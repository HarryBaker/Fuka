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

        predictList = sorted(predictList,key=itemgetter(0),reverse=True)
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






