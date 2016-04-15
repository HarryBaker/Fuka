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




