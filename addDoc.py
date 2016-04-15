__author__ = 'loaner'
import gensim
import nltk
from nltk.corpus import stopwords
from gensim import models
from gensim.models.doc2vec import TaggedDocument

import re

nltk.download("stopwords")

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
        #nltk.download("stopwords")
        self.stop = stopwords.words('english')

        if id == "help":
            self.stop.remove("not")
            self.stop.remove("don")
            #self.stop.remove("no")


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

        self.masterSentances = []
        self.boosterSentances = []

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
                newSentances = topic.addDoc(doc)
                self.masterSentances += newSentances
                if id == 'all':
                    self.boosterSentances += newSentances




