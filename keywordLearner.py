__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus
from operator import itemgetter
import re

from cleanTxtFiles import Cleaner
from SpellerCorrector import Corrector

class solutionTrainer:
    def __init__(self, sentences, cutoff):
        self.sentences = sentences
        self.possibleSolutions = []
        self.listOfModels = []
        self.unknownCutoff = cutoff

        self.modelMaster = models.Doc2Vec(self.sentences, size=600, window=8, min_count=10)


    def createModel(self, docs, prompt):

        model = models.Doc2Vec(docs + docs + self.sentences, size=100, window=8, min_count = 5)
        self.listOfModels.append((prompt, model))

    def compareSimilarity(self, query, option, model):
        queryList = query
        queryListFinal = []

        optionList = option
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
            if word not in model.vocab:
                correctedWord = spellChecker.correct(word)
            else:
                correctedWord = word
            if correctedWord in model.vocab:
                queryListFinal.append(correctedWord)



        for word in optionList:
            if word in model.vocab:
                optionListFinal.append(word)


        print "Final Query"
        print queryListFinal

        if queryListFinal:
            score = model.n_similarity(queryListFinal, optionListFinal)
            return score
        else:
            return 0


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

        for stuff in self.listOfModels:
            sim = self.compareSimilarity(query, stuff[0].split(), stuff[1])
            #rank = self.compareSimilarity(query, solution)
            predictList.append((sim, stuff[0]))

        return predictList




