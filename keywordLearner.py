__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus
from operator import itemgetter
import re

from cleanTxtFiles import Cleaner
from SpellerCorrector import Corrector

#working with one model
class solutionTrainer:
    def __init__(self, sentences, cutoff):
        self.sentences = sentences
        self.possibleSolutions = []
        self.listOfModels = [] #maybe should be a Hash?
        self.unknownCutoff = cutoff

        #Question is do we want individual models for each possible, or one master model?
        #Lest
        self.modelMaster = models.Doc2Vec(self.sentences, size=600, window=8, min_count=10)


    def createModel(self, docs, prompt):

        model = models.Doc2Vec(docs + docs + self.sentences, size=100, window=8, min_count = 5)
        self.listOfModels.append((prompt, model))

    def compareSimilarity(self, query, option, model):
        queryList = query
        queryListFinal = []

        #optionList = option.split()
        optionList = option
        optionListFinal = []

        #I'm not sure why this doesn't wor. removing a word from the list skips a word
        #for word in queryList:
        #    if word not in self.model.vocab:
        #        queryList.remove(word)

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

        for item in query:
            if "not" in item:
                query.remove(item)

        newQuery = " ".join(query)

        query = filter(None, re.split("[, \-!?:]+", newQuery))

        #for solution in self.possibleSolutions:
        for stuff in self.listOfModels:
            sim = self.compareSimilarity(query, stuff[0].split(), stuff[1])
            #rank = self.compareSimilarity(query, solution)
            predictList.append((sim, stuff[0]))

 #       outputlist = sorted(predictList, key=itemgetter(0), reverse=True)


#        prediction = predictList[0]

  #      if prediction[1] < self.unknownCutoff:
   #         prediction = "Unknown"

        return predictList




