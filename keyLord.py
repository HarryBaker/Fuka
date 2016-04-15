__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus
from operator import itemgetter
import re

from cleanTxtFiles import Cleaner
from SpellerCorrector import Corrector


class Model():
    def __init__(self, id, model):
        self.id = id
        self.doc2vecModel = model

class solutionTrainer:
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
            neuralModel = models.Doc2Vec(topic.allSentances + topic.allSentances, size=100, window=8, min_count = )
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

        return predictList

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



class Topic():
    def __init__(self, id):
        self.id = id
        self.listOfDocuments = []
        self.numDocs = 0

        self.allSentances = []

        nltk.download("stopwords")
        self.stop = stopwords.words('english')

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

    def addDoc(self,doc):
        self.listOfDocuments.append(doc)
        self.numDocs += 1
        return self.createSentances(doc)




    def createSentances(self, doc):
        #break document into list of sentances to feed to word2doc
        #maybe label sentances that include the search.
        #Sentances must be lists of individual words. A document is a list of these lists

        sentances = []

        lines = [line.rstrip('\n') and line.rstrip(' ') for line in open(doc)]

        for line in lines:
            x = filter(None, re.split("[,\-!?:]+", line))
            for sentance in x:
                y = sentance.lower().split()
                sentanceToAdd = []
                for word in y:
                    if word and word not in self.stop:
                        if word in self.pluralsList:
                            word = self.pluralsList[word]
                        sentanceToAdd.append(word)
                TD = TaggedDocument(tags=self.id.split(), words=sentanceToAdd)
                sentances.append(TD)

        self.allSentances = self.allSentances + sentances
        return sentances


class trainingCorpus:
    def __init__(self):
        self.topics = []
        self.numberOfTopics = 0

        self.listOfDocs = []
        self.numberOfDocs = 0

        self.masterSentance = []
        self.topicSentances = {}


    def addTopic(self, name):
        newTopic = Topic(name)
        self.topics.append(newTopic)
        self.numberOfTopics += 1


    def addDoc(self, doc, id):
        self.listOfDocs.append((doc,id))
        self.numberOfDocs +=1

        for topic in self.topics:
            if id == topic.id:
                self.masterSentance += topic.addDoc(doc)




