__author__ = 'loaner'
import gensim
import nltk
from nltk.corpus import stopwords
from gensim import models
from gensim.models.doc2vec import TaggedDocument

import re



class trainingCorpus:
    def __init__(self):
        self.listOfVocabs = []

        

        self.listOfDocs = []
        self.numberOfDocs = 0


    def addVocab(self, id):


    def addDoc(self, doc, id):
        self.listOfDocs.append((doc,id))
        self.numberOfDocs +=1




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
            x = filter(None, re.split("[,\-!?:]+", line))
            for sentance in x:
                y = sentance.lower().split()
                sentanceToAdd = []
                for word in y:
                    if word and word not in stop:
                        if word in pluralsList:
                            word = pluralsList[word]
                        sentanceToAdd.append(word)
                TD = TaggedDocument(tags=id, words=sentanceToAdd)
                sentances.append(TD)

        return sentances



