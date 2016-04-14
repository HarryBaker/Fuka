__author__ = 'loaner'

__author__ = 'loaner'
from gensim import models
from addDoc import trainingCorpus
from operator import itemgetter
import re

from cleanTxtFiles import Cleaner


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

        for word in queryList:
            if word in pluralsList:
                    word = pluralsList[word]
            if word in model.vocab:
                queryListFinal.append(word)



        for word in optionList:
            if word in model.vocab:
                optionListFinal.append(word)

        if queryListFinal:
            score = model.n_similarity(queryListFinal, optionListFinal)
            return score
        else:
            return 0


    def predictMethod(self, query):

        predictList = []

        query = filter(None, re.split("[, \-!?:]+", query))

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




if __name__ == '__main__':
    CS = trainingCorpus()
    FQ = trainingCorpus()
    QF = trainingCorpus()
    SR = trainingCorpus()
    EM = trainingCorpus()
    SM = trainingCorpus()
    BU = trainingCorpus()
    #t.addDoc('WikiQuadraticEquation')
    #t.addDoc('CompleteSquareWiki')
    #t.addDoc('FactorizationWiki')
    #t.addDoc('SquareRootWiki')
    BU.addDoc('backup', ['All'])



    CS.addDoc('completeSquare_clean.txt', ['complete', 'square'])
    EM.addDoc('eliminationMethod_clean.txt', ['elimination', 'method'])
    FQ.addDoc('factorQuadratic_clean.txt', ['factor', 'square'])
    QF.addDoc('quadraticFormula_clean.txt', ['quadratic', 'formula'])
    SM.addDoc('substitutionMethod_clean.txt', ['substitution', 'method'])
    SR.addDoc('takeSquareRoot_clean.txt', ['take', 'square', 'root'])



    sentencesCS = CS.createSentances()
    sentencesFQ = FQ.createSentances()
    sentencesQF = QF.createSentances()
    sentencesSR = SR.createSentances()
    sentencesSM = SM.createSentances()
    sentencesEM = EM.createSentances()
    sentencesBU = BU.createSentances()



    stuff = solutionTrainer(sentencesCS + sentencesFQ + sentencesQF + sentencesSR + sentencesBU + sentencesBU
                            + sentencesBU, .3)

    stuff.createModel(sentencesCS, 'complete square')
    stuff.createModel(sentencesFQ, 'factor quadratic')
    stuff.createModel(sentencesQF, 'quadratic formula')
    stuff.createModel(sentencesSR, 'square root')
    #stuff.createModel(sentencesSM, 'substitution method')
    #stuff.createModel(sentencesEM, 'elimination method')


    #stuff.possibleSolutions.append('quadratic formula')
    ##stuff.possibleSolutions.append('complete the square')
    #stuff.possibleSolutions.append('take square root')
    #stuff.possibleSolutions.append('factor the quadratic')
    #stuff.possibleSolutions.append('elimination method')
    #stuff.possibleSolutions.append('substitution method')



    aa = stuff.predictMethod('complete-the-squares method')
    ab = stuff.predictMethod('complete-the-square method')
    ac = stuff.predictMethod('complete the squares method')
    ad = stuff.predictMethod('complete the square method')


    ae = stuff.predictMethod("i want to replace stuff in the equation")
    af = stuff.predictMethod("i want to break apart the equation")
    ag = stuff.predictMethod('lets do the square root')
    ah = stuff.predictMethod('i want to square it')
    ai = stuff.predictMethod('use the complete the squares method')
    aj = stuff.predictMethod('i\'ll use the method of completing the squares')
    ak = stuff.predictMethod('komplete da skware')
    al = stuff.predictMethod('i\'m not sure')
    am = stuff.predictMethod('complete-the-squares method')
    an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    ao = stuff.predictMethod('dunno, maybe quadratic?')
    ap = stuff.predictMethod('i\'ll factor quadratics')
    aq = stuff.predictMethod('i plan to complete the squares')
    ar = stuff.predictMethod('do a square root')
    at = stuff.predictMethod('i have no idea')
    au = stuff.predictMethod('help')
    av = stuff.predictMethod('Xyzzy')
    aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    ay = stuff.predictMethod('Consult the i ching')
    az = stuff.predictMethod('Read Tea Leaves')


    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')



    print "done"
    print aa


__author__ = 'loaner'
import gensim
import nltk
from nltk.corpus import stopwords
from gensim import models
from gensim.models.doc2vec import TaggedDocument

import re



class trainingCorpus:
    def __init__(self):
        self.listOfDocs = []
        self.numberOfDocs = 0

    def addDoc(self, doc, id):
        #add document to corpus. Clear stopwords, or will doc2vec do that for us?
        #mybe search threw and only include sentances that matter, ie, that include the word of one of the options?
        #like search threw doc, and only include sentances that include "Quadratic"
        #if we're only doing one document, then we shouldn't need to search.
        self.listOfDocs.append((doc,id))
        self.numberOfDocs +=1
        #break it up into sentances now or later? Later I think. this just compiles list of docs

    def createSentances(self):
        totalSentances = []


        for doc,id in self.listOfDocs:
            x = self.sentanceBreak(doc, id)
            totalSentances = totalSentances + x

        return totalSentances

    def sentanceBreak(self, doc, id):
        #break document into list of sentances to feed to word2doc
        #maybe label sentances that include the search.
        #Sentances must be lists of individual words. A document is a list of these lists

        sentances = []

        #with open(doc, 'r') as fileinput:
        #    for line in fileinput:
        #        line = line.lower()

        #fileinput.close()
        ##file_content = open(doc, "r")
        #file_content = [line.lower() for line in file_content]
        #with open(doc, 'w') as out:
        #    out.writelines(sorted(file_content))


        #words = file_content.read().split

        #for line in words:
        #    for word in line:
        #        word.lower()
        #file_content.close()

        #y = gensim.models.doc2vec.TaggedLineDocument(doc)
        #y.__iter__()
        lines = [line.rstrip('\n') and line.rstrip(' ') for line in open(doc)]

        nltk.download("stopwords")
        stop = stopwords.words('english')

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



        for line in lines:
            #x = line.split(".")
            x = filter(None, re.split("[,\-!?:]+", line))
            for sentance in x:
                y = sentance.lower().split()
                sentanceToAdd = []
                for word in y:
                    if word and word not in stop:
                    #y = gensim.models.doc2vec.TaggedDocument(words = y, labels = [""])
                    #y = models.Doc2Vec.LabeledSentence(words = y)
                        if word in pluralsList:
                            word = pluralsList[word]
                        sentanceToAdd.append(word)
                TD = TaggedDocument(tags=id, words=sentanceToAdd)
                sentances.append(TD)

        return sentances

