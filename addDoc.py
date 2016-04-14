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



