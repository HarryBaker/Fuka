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

#Booster sentances are sentances for phrases that we believe will be more expected than otherwise found in an
#unstructured corpus. For example, if you want to teach the model that "I want to break apart the function" is
#associated with the method "factor the quadratic", then you would manually write language in the booster document
#to encourage this association in a more supervised fashion. While our booster training does increase the
#similarity of certain prompts like this in intended ways, it does not have enough training to push the
#similarity ranking above the designated threshold in all cases. For example, "i want to break apart the function'
#matches 'quadratic formula', which is close, but not totally ideal This needs more work, but seems like an effective.
#way to identify common phrases and synonyms.
class SolutionTrainer:
    def __init__(self, trainingMaterial, cutoff):
        self.unknownCutoff = cutoff
        self.trainingMaterial = trainingMaterial

        self.topics = trainingMaterial.topics
        self.masterSentances = trainingMaterial.masterSentances
        self.boosterSentances = trainingMaterial.boosterSentances


        self.listOfModels = []


        #Similar to the Topic class. Dictionary of commonly used words and their plurals,
        #to convert plurals into their singular equivalient.
        self.varientList = {
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
            'substitute' : 'substitution',
            'substituting' : 'substitution',
            'substituted' : 'substitution',
            'eliminate' : 'elimination',
            'eliminated' : 'elimination',
            'eliminating' : 'elimination',
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
            neuralModel = models.Doc2Vec(topic.allSentances * 7 + self.masterSentances + self.boosterSentances *20, size=100, window=8, min_count = 5)
        model = Model(topic.id, neuralModel)
        self.listOfModels.append(model)

    #Given a query, predicts which method it is most closely related to.
    def predictMethod(self, query):

        predictList = []

        #Splits on "not" so as to identify negations in the query
        #Ie, i want to do the quadratic equation, not factor the quadratic
        #The following two for loops go through and remove the parts of the sentance following "not".
        #This is a very basic way of checking for negations, and could use more work to be more nuanced.
        #For example, it doesn't handle sentances with multiple nots very well, and it doesn't recognize negative
        #words other than not.

        #This is all especially true if adapting to languages that have a different sentance structure than English.

        #as mentioned in addDoc.py, doc2vec has a way to affect the ranking the significance of a sentance by negatively
        #weighing it against certain keywords. There might be some application here for that.
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


        #Compares the similarity of the query to each potential method by running through each method's corresponging 
        #neural model.
        for model in self.listOfModels:
            sim = self.compareSimilarity(query, model)
            predictList.append([sim, model.id])


        #Sorts the possible methods in descending order from highest to lowest confidence. It returns the first element
        #of the list, which is the most similar method to the query. It only returns one method; if you want to return
        #multiple methods (if the query is ambiguious--"i want to do quadratic", ie) you can implement a threshold
        #that will only pass high enough confidence answers
        predictList = sorted(predictList,key=itemgetter(0),reverse=True)
        prediction = predictList[0]

        #If the prediction doesn't have a high enough confidence, return that it's unknown.txt.
        #There are some issues here with the "help" class, because even when "help" is the most strongly associated
        #choice, it doesn't make the threshold. This can probably be fixed by training more "help" documents
        if prediction[1] == 'help':
            if prediction[0] < .2:
                prediction[1] = "Unknown"
        else:
            if prediction[0] < self.unknownCutoff:
                prediction[1] = "Unknown"

        return (query, prediction)

    #Compares the similarity of the query to the method associated with each model.
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
            if word in self.varientList:
                    word = self.varientList[word]
            #If word is not recognized, try correcting it's spelling
            if word not in model.doc2vecModel.vocab:
                correctedWord = self.spellChecker.correct(word)
            else:
                correctedWord = word
            #If corrected word is in the model's vocabular, include it. You can't try to find the similarity of words
            #that aren't in the model's vocabulary, or it will crash. One problem here though is that some gibberish
            #words are simply cut out if they can't be properly spellchecked, so the query might give a false positive.
            #This is what happens with the mispelled "I might use the substitutittiion method" query in the demo.
            #It is not identified as supstitution, so the only significant words that are passed are "might" and
            #"method", which match more closely to the elimination method in most cases.
            #Adding some kind of "unknownWord" token might fix this by weighting down queries with a lot of
            #unknown.txt words, or by measuring them against a document only including the word "unknownWord",
            #but we couldn't figure out how to implement it.
            #
            #For some reason however, leaving the documents and topics associated with "unknown.txt" seems to
            #work for the cases we initially tested against (specifically the misspelled substitution query).
            #We're not sure why this works; the additional noise might only specifically help in this case, or the
            #additional noise might be just enough padding to prevent a query from becoming too closely associated with
            #false positives.
            #One issue, however, is this noise prevents recognition of the inputs 'i want to break apart the equation'
            #and i'll find what the factors are' if the threshold is too low. We believe it might also disturb
            #similarly ambiguous inputs. We've left the "unknown.txt" in our demo, but more developed implementations
            #of this code with more nuanced training documents should probably remove it.
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
        #If there are no words recognized in the query, return 0, which will result in unknown.txt.
        else:
            return 0






