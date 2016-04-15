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

#
class SolutionTrainer:
    def __init__(self, trainingMaterial, cutoff):
        self.unknownCutoff = cutoff
        self.trainingMaterial = trainingMaterial

        self.topics = trainingMaterial.topics
        self.masterSentances = []

        for topic in self.topics:
            self.masterSentances += topic.allSentances

        self.listOfModels = []
        self.modelMaster = models.Doc2Vec(self.trainingMaterial.masterSentance, size=600, window=8, min_count=10)

        for topic in self.topics :
            if topic.id != 'all':
                self.createModel(topic)



    #def createModel(self, docs, prompt):
    def createModel(self,topic):

        if topic.id == 'help':
            neuralModel = models.Doc2Vec(topic.allSentances + topic.allSentances, size=10, window=8, min_count = 1)
        else:
            neuralModel = models.Doc2Vec(topic.allSentances + topic.allSentances + self.masterSentances, size=100, window=8, min_count = 5)
        model = Model(topic.id, neuralModel)
        self.listOfModels.append(model)

    def predictMethod(self, query):

        predictList = []
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

        query = filter(None, re.split("[, \-!?:]+", query))

        for model in self.listOfModels:
            sim = self.compareSimilarity(query, model)
            #rank = self.compareSimilarity(query, solution)
            predictList.append((sim, model.id))

        return (query, predictList)

    def compareSimilarity(self, query, model):
        queryList = query
        queryListFinal = []

        optionList = model.id.split()
        optionListFinal = []

        pluralsList = {
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



        spellChecker = Corrector('big.txt')

        for word in queryList:
            if word in pluralsList:
                    word = pluralsList[word]
            if word not in model.doc2vecModel.vocab:
                correctedWord = spellChecker.correct(word)
            else:
                correctedWord = word
            if correctedWord in model.doc2vecModel.vocab:
                queryListFinal.append(correctedWord)



        for word in optionList:
            if word in model.doc2vecModel.vocab:
                optionListFinal.append(word)


        if queryListFinal:
            score = model.doc2vecModel.n_similarity(queryListFinal, optionListFinal)
            return score
        else:
            return 0

__author__ = 'loaner'
import gensim
import nltk
from nltk.corpus import stopwords
from gensim import models
from gensim.models.doc2vec import TaggedDocument

import re



#Class to hold onto list of topics and their associated documents. That is, the topic "quadratic equation" would have a
#list of all documents associated into it. It will also store these documents as a list of sentances to be fed to
#the doc2vec model
class Topic():
    def __init__(self, id):
        self.id = id
        self.listOfDocuments = []
        self.numDocs = 0

        #list of sentances prepped for doc2vec. Sentances must be stored as a list of words. Each sentance is tagged
        #with the topic's id to give supervised structure to the learning algorithm.
        self.allSentances = []

        #common stopwords to be removed from each sentance. Extra stopwords can be added
        nltk.download("stopwords")
        self.stop = stopwords.words('english')

        #Converts plurals to singulars to help with training. Since plural and singular words are considered completely
        #different words. Additional training might make this unnesesary if the neural network is taught to connect
        #plurals
        #This should be moved to the training corpus class and passed to topics since it's common for all.
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

    #Add document to a topic and prepare it's sentances for training
    def addDoc(self,doc):
        self.listOfDocuments.append(doc)
        self.numDocs += 1
        return self.createSentances(doc)



    #prepares documents for training to feed to doc2vec. In future developent, you can add the ability to tag sentances
    #with other keywords to fine tune the supvervised training. Currently sentances are only tagged with the ID of their
    #topic
    def createSentances(self, doc):

        sentances = []

        lines = [line.rstrip('\n') and line.rstrip(' ') for line in open(doc)]

        for line in lines:
            #Splits the line at different punctuation.
            lineSentances = filter(None, re.split("[.\-!?:]+", line))
            for sentance in lineSentances:
                #splits sentance into constituent words and makes them lowercase
                splitSentance = sentance.lower().split()
                sentanceToAdd = []
                for word in splitSentance:
                    #Checks if word is in the stoplist
                    if word not in self.stop:
                        #checks if a comma follows a word, and removes it if it does.
                        if "," in word:
                            addWord = word[:-1]
                        else:
                            addWord = word
                        #Converts plural key words to their singular form.
                        if addWord in self.pluralsList:
                            addWord = self.pluralsList[addWord]
                        else:
                            addWord = addWord

                        sentanceToAdd.append(addWord)
                #doc2vec sentances must be tagged to aid in training. Additional tags can be added here.
                TD = TaggedDocument(tags=self.id.split(), words=sentanceToAdd)
                sentances.append(TD)

        #Updates total sentances for the topic, and returns the specific sentance
        self.allSentances = self.allSentances + sentances
        return sentances


#Class to prep the total training corpus to feed to the neural network. It includes the sentances for each specific
#topic, as well as a master list of all sentances included.
class trainingCorpus:
    def __init__(self):
        self.topics = []
        self.numberOfTopics = 0

        self.listOfDocs = []
        self.numberOfDocs = 0

        self.masterSentance = []

    #add potential topic to list of topics to train for
    def addTopic(self, name):
        newTopic = Topic(name)
        self.topics.append(newTopic)
        self.numberOfTopics += 1

    #adds documents to associated topic, which then preps the sentance. The prepped sentance is then included in the
    #master sentance
    def addDoc(self, doc, id):
        self.listOfDocs.append((doc,id))
        self.numberOfDocs +=1

        #there's probably a more effecient way to grab the associated topic. Python doesn't like it when we use our
        #ID's as a key in a hash table because their strings.
        for topic in self.topics:
            if id == topic.id:
                self.masterSentance += topic.addDoc(doc)




__author__ = 'loaner'
from addDoc import trainingCorpus
from keywordLearner import solutionTrainer
from SpellerCorrector import Corrector


if __name__ == '__main__':


    TC = trainingCorpus()
    TC.addTopic('complete square')
    TC.addTopic('factor quadratic')
    TC.addTopic('take square root')
    TC.addTopic('quadratic formula')
    TC.addTopic('help')
    TC.addTopic('all')



    TC.addDoc('backup', 'all')
    TC.addDoc('completeSquare_clean.txt', 'complete square')
    TC.addDoc('factorQuadratic_clean.txt', 'factor quadratic')
    TC.addDoc('quadraticFormula_clean.txt', 'quadratic formula')
    TC.addDoc('takeSquareRoot_clean.txt', 'take square root')
    TC.addDoc('Help.txt', 'help')


    model = solutionTrainer(TC, .3)


    #aa = model.predictMethod("I want to do the quadratic formula")
    #ab = model.predictMethod("I want to do the qudratic formula")
    ac = model.predictMethod("I want to do the quadrtic formula")
    help = model.predictMethod("help me i don't know what to do")
    ad = model.predictMethod("I want to do the queadrtic formula")
    ae = model.predictMethod(("I want to do the quadratic formula, not factor the quadratic"))
    af = model.predictMethod('lets do the square root')



    ag = model.predictMethod('complete-the-squares method')
    ah = model.predictMethod('complete-the-square method')
    #ac = stuff.predictMethod('complete the squares method')
    #ad = stuff.predictMethod('complete the square method')


    #ae = stuff.predictMethod("i want to replace stuff in the equation")
    #bf = model.predictMethod("i want to break apart the equation")
    #ag = stuff.predictMethod('lets do the square root')
    #ah = stuff.predictMethod('i want to square it')
    #ai = model.predictMethod('use the complete the squares method')
    #aj = model.predictMethod('i\'ll use the method of completing the squares')
    #ak = model.predictMethod('komplete da skware')
    #al = model.predictMethod('i\'m not sure')
    #am = stuff.predictMethod('complete-the-squares method')
    #an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    ##ao = stuff.predictMethod('dunno, maybe quadratic?')
    #ap = model.predictMethod('i\'ll factor quadratics')
    #aq = stuff.predictMethod('i plan to complete the squares')
    ##ar = stuff.predictMethod('do a square root')
    #at = model.predictMethod('i have no idea')
    #au = model.predictMethod('help')
    #av = stuff.predictMethod('Xyzzy')
    #aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    #ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    #ay = model.predictMethod('Consult the i ching')
    #z23 = stuff.predictMethod('Read Tea Leaves')

    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')






    print "done"
    #print ae







