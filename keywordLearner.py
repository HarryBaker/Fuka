__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus
from operator import itemgetter
import re

from cleanTxtFiles import Cleaner
from SpellerCorrector import Corrector


#Class to hold the doc2vecModel of each topic. The id's are the potential methods: ie, "factor the quadratic"
#The model is the actual doc2vec neural network.
#Gensim tutorials do a better job explaining how doc2vec works than I ever could
#doc2vec works almost identically to word2vec, except the sentances are given tags
# http://rare-technologies.com/word2vec-tutorial/
#documentation
#https://radimrehurek.com/gensim/models/doc2vec.html
class Model():
    def __init__(self, id, model):
        self.id = id
        self.doc2vecModel = model


#SolutionTrainer holds all of the models that we want to use to analyze our queries with. Each topic has it's own
# doc2vec neural network that it is trained with. These neural networks are trained on the documents that are associated
#specifically with the topic, as well as the master list of sentances. This allows us to train on a broader base of
#knowledge, while giving special influence to documents that are more closely associated with the topic.

#Booster sentances are sentances for uses that we believe will be more expected than otherwise found in an unstructured
#corpus. For example, if you want to teach the model that "I want to break apart the function" is associated with
#the method "factor the quadratic", then you would manually write language in the booster document to lead to this more
#nuanced semantic understanding of the prompt. While our booster training can increase the similarity of these prompts
#in intended ways, it does not have enough training to push the ranking above the threshold. This needs more work.
class SolutionTrainer:
    def __init__(self, trainingMaterial, cutoff):
        self.unknownCutoff = cutoff
        self.trainingMaterial = trainingMaterial

        self.topics = trainingMaterial.topics
        self.masterSentances = trainingMaterial.masterSentances
        self.boosterSentances = trainingMaterial.boosterSentances

        #for topic in self.topics:
        #    self.masterSentances += topic.allSentances

        self.listOfModels = []


        #Similar to the Topic class. Dictionary of commonly used words and their plurals,
        #to convert plurals into their singular equivalient.
        self.pluralsList = {
            'squares' : 'square',
            'squaring' : 'square',
            'squared' : 'square',
            'quadratics' : 'quadratic',
            'roots' : 'root',
            'factors' : 'factor',
            'factoring' : 'factor',
            'factorize' : 'factor',
            'factored' : 'factor',
            'completes' : 'complete',
            'completing' : 'complete',
            'completed' : 'complete',
        }

        #Object to spellcheck words. This also depends on the text you use to train it. Most of the text
        #in our included file is general use--it is based off of Sherlock Holme's novels--so it might
        #not recognize specific mathwords. This is easily fixed by including multiple instances of the specific
        #word at the beginning of the document. For future uses it would probably be better to train this on
        #more math oriented documents.
        self.spellChecker = Corrector('big.txt')

        #For more information on size and mincounts, see the documentation for doc2vec
        self.modelMaster = models.Doc2Vec(self.masterSentances, size=600, window=8, min_count=10)

        for topic in self.topics :
            #Doesn't include the general topic, since that just stores documents that aren't saved to a particular topic
            if topic.id != 'all':
                self.createModel(topic)


    #Create's a peronalized doc2vec model for each topic
    def createModel(self,topic):

        #Run specialized run of the "help" topic. This one is more sentsative to specific key words, so we don't
        #include the master sentances so as to not dilute the influence of specific key "help" words. This particular
        #topic needs more work and training.
        if topic.id == 'help':
            neuralModel = models.Doc2Vec(topic.allSentances * 1000, size=20, window=8, min_count = 1)
        else:
            neuralModel = models.Doc2Vec(topic.allSentances * 7 + self.masterSentances + self.boosterSentances *10, size=100, window=8, min_count = 5)
        model = Model(topic.id, neuralModel)
        self.listOfModels.append(model)

    #Given a query, predicts which method it is most closely related to.
    def predictMethod(self, query):

        predictList = []

        #Splits on "Not" so as to identify negations in the query
        #Ie, i want to do the quadratic equation, not factor the quadratic
        #The following two for loops go through and remove the parts of the sentance following not.
        #This is a very basic way of checking for negations, and could use more work to be more nuanced. This
        #is especially true if adapting to languages that have a different sentance structure than english

        #doc2vec has a way to negatively
        query = query.split("not")

        tempQuery = []
        for i in range(0,len(query)):
            if i >= 1:
                tempQuery.append("not" + query[i])
            else:
                tempQuery.append(query[i])

        for item in tempQuery:
            if "not" in item:
                tempQuery.remove(item)

        query = " ".join(tempQuery)

        #Splits query into a list of words, removing puncuation
        query = filter(None, re.split("[., \-!?:]+", query))


        #Compares the similarity of the query to each potential method.
        #It does this by running through each method's corresponging neural model.
        for model in self.listOfModels:
            sim = self.compareSimilarity(query, model)
            predictList.append([sim, model.id])


        #Sorts the possible methods in descending order from highest to lowest confidence. It returns the first element
        #of the list, which is the most similar method to the query. It only returns one method; if you want to return
        #multple methods (if the query is ambiguious--"i want to do quadratic", ie) you can implement a threshold
        #that will only pass high enough confidence answers
        predictList = sorted(predictList,key=itemgetter(0),reverse=True)
        prediction = predictList[0]

        #If the prediction doesn't have a high enough confidence, return that it's unknown.
        #There are some issues here with the "help" class, because even when "help" is the most strongly associated
        #choice, it doesn't make the threshold. This can probably be fixed by training more "help" documents
        if prediction[1] == 'help':
            if prediction[0] < .2:
                prediction[1] = "Unknown"
        else:
            if prediction[0] < self.unknownCutoff:
                prediction[1] = "Unknown"

        return (query, prediction)

    #compares the similarity of the query to the method associated with each model.
    #For example, self.compareSimilarity("quadraticMethod", squareRootModel) would find the similarity of
    #"quadraticMethod" to "square root" using the square root neural network
    def compareSimilarity(self, query, model):
        queryList = query
        queryListFinal = []

        #the option is the method associated with the model, which is stored as it's ID
        #splitting it into sentances allow's doc2vec to understand it
        optionList = model.id.split()
        optionListFinal = []


        for word in queryList:
            #Convert plural words to singular
            if word in self.pluralsList:
                    word = self.pluralsList[word]
            #If word is not recognized, try correcting it's spelling
            if word not in model.doc2vecModel.vocab:
                correctedWord = self.spellChecker.correct(word)
            else:
                correctedWord = word
            #If corrected word is in the model's vocabular, include it. You can't try to find the similarity of words
            #that aren't in the model's vocabulary, or it will crash.
            if correctedWord in model.doc2vecModel.vocab:
                queryListFinal.append(correctedWord)

        #Sanity check to make sure that the words for each method are included in the model's vocabulary. Since
        #The method's name is used as a tag for each included sentance, they will probably always be found.
        for word in optionList:
            if word in model.doc2vecModel.vocab:
                optionListFinal.append(word)

        #If there are words left in the the query, find their similarity to the given method.
        if queryListFinal:
            score = model.doc2vecModel.n_similarity(queryListFinal, optionListFinal)
            return score
        #If there are no words recognized in the query, return 0, which will result in unknown.
        else:
            return 0






