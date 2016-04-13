__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus


#working with one model
class solutionTrainer:
    def __init__(self, sentences, cutoff):
        self.sentences = sentences
        self.possibleSolutions = []
        self.listOfModels = [] #maybe should be a Hash?
        self.unknownCutoff = cutoff

        #Question is do we want individual models for each possible, or one master model?
        #Lest
        self.model = models.Word2Vec(self.sentences, size=200, window=8, min_count=2)

    def compareSimilarity(self, query, option):
        queryList = query.split()
        queryListFinal = []

        optionList = option.split()
        optionListFinal = []

        #I'm not sure why this doesn't wor. removing a word from the list skips a word
        #for word in queryList:
        #    if word not in self.model.vocab:
        #        queryList.remove(word)

        for word in queryList:
            if word in self.model.vocab:
                queryListFinal.append(word)

        for word in optionList:
            if word in self.model.vocab:
                optionListFinal.append(word)


        score = self.model.n_similarity(queryListFinal, optionListFinal)
        return score


    def predictMethod(self, query):

        predictList = []

        for solution in self.possibleSolutions:
            sim = self.compareSimilarity(query, solution)
            #rank = self.compareSimilarity(query, solution)
            predictList.append((solution, sim))

        #sorted(predictList, key=(2))

        #prediction = predictList[0]

        #if prediction[1] < self.unknownCutoff:
        #    prediction = "Unknown"

        return predictList




if __name__ == '__main__':
    t = trainingCorpus()
    #t.addDoc('WikiQuadraticEquation')
    #t.addDoc('CompleteSquareWiki')
    #t.addDoc('FactorizationWiki')
    #t.addDoc('SquareRootWiki')
    t.addDoc('backup')

    sentences = t.createSentances()
    stuff = solutionTrainer(sentences, .3)
    stuff.possibleSolutions.append('quadratic formula')
    stuff.possibleSolutions.append('complete the square')
    stuff.possibleSolutions.append('take square root')
    stuff.possibleSolutions.append('factor the quadratic')


    y = stuff.predictMethod("i want to break apart the function.")


    print "done"
    print y


