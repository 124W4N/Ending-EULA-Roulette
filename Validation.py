# Validating using Hold-Out 80-20
from __future__ import division, unicode_literals
import math, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk
from nltk.classify import ClassifierI



DIR1 = 'DatasetCorpus/pos/'
DIR2 = 'DatasetCorpus/neg/'
posSet = os.listdir(DIR1)
negSet = os.listdir(DIR2)
import random
random.shuffle(posSet)
random.shuffle(negSet)


def tf(word, tokens):
    return (float)(tokens.count(word)) / (float)(len(tokens))


def n_containing(word, posSet):
    return (float)(sum(1 for fileid in posSet if word in nltk.word_tokenize(fileid)))


def idf(word, posSet):
    length = []
    for fileid in posSet:
        length.append(nltk.word_tokenize(fileid))
    return (float)(math.log(len(length)) / (float)((1 + n_containing(word, posSet))))


def tfidf(word, tokens, posSet):
    return (float)(tf(word, tokens)) * (float)(idf(word, posSet))



def pos_word_feats_train(file):
    scores = {}
    x = {}
    with open(DIR1 + file, 'r') as posSentences:
        for fileid in posSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, posSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[ 1 ], reverse=True)
            for word, score in sorted_words[ :30 ]:
                x.update([ (word, True) ])

    return x

def pos_word_feats_test(file):
    scores = {}
    x = {}
    with open(DIR1 + file, 'r') as posSentences:
        for fileid in posSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, posSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[ 1 ], reverse=True)
            for word, score in sorted_words[ :30 ]:
                x.update([ (word, True) ])

    return x
PosTrainSet=int(len(posSet) * 4/5)
posfeatstrain = [(pos_word_feats_train(file), 'pos') for file in posSet[:PosTrainSet]]
posfeatstest = [(pos_word_feats_test(file)) for file in posSet[PosTrainSet:]]
Accuracyposfeatstest = [(pos_word_feats_test(file), 'pos') for file in posSet[PosTrainSet:]]


def neg_word_feats_train(file):
    scores = {}
    x = {}
    with open(DIR2 + file, 'r') as negSentences:
        for fileid in negSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, negSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[ 1 ], reverse=True)
            for word, score in sorted_words[ :30 ]:
                x.update([ (word, True) ])
                #                 Top5negFeatures.append([word, round(score, 5)])
    return x
def neg_word_feats_test(file):
    scores = {}
    x = {}
    with open(DIR2 + file, 'r') as negSentences:
        for fileid in negSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, negSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[ 1 ], reverse=True)
            for word, score in sorted_words[ :30 ]:
                x.update([ (word, True) ])
                #                 Top5negFeatures.append([word, round(score, 5)])
    return x


NegTrainSet=int(len(negSet) * 4/5)
negfeatstrain = [(neg_word_feats_train(file), 'neg') for file in negSet[:NegTrainSet]]
negfeatstest = [(neg_word_feats_test(file)) for file in negSet[NegTrainSet:]]
Accuracynegfeatstest = [(neg_word_feats_test(file), 'neg') for file in negSet[NegTrainSet:]]


trainfeats = posfeatstrain+negfeatstrain
testfeats = posfeatstest+ negfeatstest
Acuraccytestfeats = Accuracyposfeatstest+Accuracynegfeatstest



class validation(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    def crossValid(self):
        for c in self._classifiers:
                print c
                clas=c.train(trainfeats)
                print clas.classify_many(testfeats)
                print (nltk.classify.util.accuracy(clas,Acuraccytestfeats)) * 100
                # for pdist in clas.prob_classify_many(testfeats):
                #     print('%.4f %.4f' % (pdist.prob('pos'), pdist.prob('neg')))
                print('-' * 15)
                print('-' * 15)

v=validation(nltk.NaiveBayesClassifier,
           SklearnClassifier(MultinomialNB()),
            SklearnClassifier(BernoulliNB()),
           SklearnClassifier(NuSVC(probability=True)),
           SklearnClassifier(SVC(probability=True)))

v.crossValid()