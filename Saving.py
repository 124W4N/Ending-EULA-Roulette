# (step 1) runs the classifiers with the training set and saves them

from __future__ import division, unicode_literals
import re, math, collections, itertools, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC


DIR1 = 'DatasetCorpus/pos/'
DIR2 = 'DatasetCorpus/neg/'
posSet = os.listdir(DIR1)
negSet = os.listdir(DIR2)
import random
random.shuffle(posSet)
random.shuffle(negSet)


def word_feats(words):
    return dict([(word, True) for word in words])


import copy

def make_hash(o):
    if isinstance(o, (set, tuple, list)):
        return tuple([make_hash(e) for e in o])
    elif not isinstance(o, dict):
        return hash(o)

    new_o = copy.deepcopy(o)
    for k, v in new_o.items():
        new_o[k] = make_hash(v)
    return hash(tuple(frozenset(sorted(new_o.items()))))


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


def pos_word_feats(file):
    scores = {}
    x = {}
    with open(DIR1 + file, 'r') as posSentences:
        for fileid in posSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, posSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:30]:
                x.update([(word, True)])

    return x

posfeats = [(pos_word_feats(file), 'pos') for file in posSet]

# -- Save to pickle --
save_posfeats= open("posfeats.pickle","wb")
pickle.dump(posfeats, save_posfeats)
save_posfeats.close()

print "im her pos"

def neg_word_feats(file):
    scores = {}
    x = {}
    with open(DIR2 + file, 'r') as negSentences:
        for fileid in negSentences:
            tokens = nltk.word_tokenize(fileid)
            for word in tokens:
                s = tfidf(word, tokens, negSet)
                results = {word: s}
                scores.update(results)
            sorted_words = sorted(scores.iteritems(), key=lambda x: x[1], reverse=True)
            for word, score in sorted_words[:30]:
                x.update([(word, True)])
                #                 Top5negFeatures.append([word, round(score, 5)])
    return x


negfeats = [(neg_word_feats(file), 'neg') for file in negSet]

# -- Save to pickle --
save_negfeats= open("negfeats.pickle","wb")
pickle.dump(negfeats, save_negfeats)
save_negfeats.close()

print "im her neg"



# posfeats_f = open("posfeats.pickle", "rb")
# posfeats = pickle.load(posfeats_f)
# posfeats_f.close()
# negfeats_f = open("negfeats.pickle", "rb")
# negfeats = pickle.load(negfeats_f)
# negfeats_f.close()

poscutoff = int(len(posfeats) * 4/5)
negcutoff = int(len(negfeats) * 4/5)

trainfeats = posfeats[ :negcutoff ] + negfeats[ :poscutoff ]
testfeats = posfeats[ negcutoff: ] + negfeats[ poscutoff: ]
#

# # -- Save to pickle --
save_trainfeats = open("trainfeats.pickle","wb")
pickle.dump(trainfeats, save_trainfeats)
save_trainfeats.close()

save_testfeats = open("testfeats.pickle","wb")
pickle.dump(trainfeats, save_testfeats)
save_testfeats.close()

print "im her3"


# -- Save to pickle --
classifier = NaiveBayesClassifier.train(trainfeats)
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(trainfeats)
# -- Save to pickle --
save_classifier = open("MNB_classifier.pickle", "wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(trainfeats)
# -- Save to pickle --
save_classifier = open("BernoulliNB_classifier.pickle", "wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(trainfeats)
# -- Save to pickle --
save_classifier = open("SVC_classifier.pickle","wb")
pickle.dump(SVC_classifier, save_classifier)
save_classifier.close()


NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(trainfeats)
# -- Save to pickle --
save_classifier = open("NuSVC_classifier.pickle","wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()
#
print "im her4"