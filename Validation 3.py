# Validating the Voting System using Hold-Out validation 60-40
from __future__ import division, unicode_literals
import os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk
from nltk.classify import ClassifierI
import scipy



DIR1 = 'DatasetCorpus/pos/'
DIR2 = 'DatasetCorpus/neg/'
posSet = os.listdir(DIR1)
negSet = os.listdir(DIR2)
import random
random.shuffle(posSet)
random.shuffle(negSet)


def pos_word_feats_train(file):
    # scores = {}
    x = {}
    with open(DIR1 + file, 'r') as posSentences:
        for fileid in posSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in nltk.FreqDist(tokens):
                x.update([ (word, True) ])

    return x

def pos_word_feats_test(file):
    # scores = {}
    x = {}
    with open(DIR1 + file, 'r') as posSentences:
        for fileid in posSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                x.update([ (word, True) ])
    return x
PosTrainSet=int(len(posSet) * 0.7)
posfeatstrain = [(pos_word_feats_train(file), 'pos') for file in posSet[:PosTrainSet]]
posfeatstest = [(pos_word_feats_test(file)) for file in posSet[PosTrainSet:]]
Accuracyposfeatstest = [(pos_word_feats_test(file), 'pos') for file in posSet[PosTrainSet:]]


def neg_word_feats_train(file):
    # scores = {}
    x = {}
    with open(DIR2 + file, 'r') as negSentences:
        for fileid in negSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in nltk.FreqDist(tokens):
                x.update([ (word, True) ])

    return x
def neg_word_feats_test(file):
    # scores = {}
    x = {}
    with open(DIR2 + file, 'r') as negSentences:
        for fileid in negSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                x.update([ (word, True) ])

    return x


NegTrainSet=int(len(negSet) * 0.7)
negfeatstrain = [(neg_word_feats_train(file), 'neg') for file in negSet[:NegTrainSet]]
negfeatstest = [(neg_word_feats_test(file)) for file in negSet[NegTrainSet:]]
Accuracynegfeatstest = [(neg_word_feats_test(file), 'neg') for file in negSet[NegTrainSet:]]


trainfeats = posfeatstrain+negfeatstrain
testfeats = posfeatstest+ negfeatstest
Acuraccytestfeats = Accuracyposfeatstest+Accuracynegfeatstest


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = [ ]
        for c in self._classifiers:
            clas = c.train(trainfeats)
            v = clas.classify(features)
            if v == "pos":
                v = 1
            elif v == 'neg':
                v = 0
            votes.append(v)
        clas = scipy.stats.mstats.mode(votes)
        if clas.mode == 1:
            print "Most voted classification: pos"
        elif clas.mode == 0:
            print "Most voted classification: neg"

        choice_votes = votes.count(clas.mode)
        Agreement = choice_votes / len(votes)
        print "Agreement:", Agreement * 100


voted_classifier = VoteClassifier(nltk.NaiveBayesClassifier,
               SklearnClassifier(MultinomialNB()),
                SklearnClassifier(BernoulliNB()),
           SklearnClassifier(NuSVC(probability=True)),
           SklearnClassifier(SVC(probability=True)))

x=0
for i in testfeats:
    x = x+1
    print x
    voted_classifier.classify(i)

