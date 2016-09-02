# (Step 1) test the trained classifiers

from __future__ import division, unicode_literals
import re, math, collections, itertools, os
import nltk.metrics
import scipy
from nltk.metrics import precision, recall, f_measure
import pickle
from nltk.classify import ClassifierI


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            if v == "pos" :
                v = 1
            elif v=='neg':
                v = 0
            votes.append(v)
        clas= scipy.stats.mstats.mode(votes)
        if clas.mode == 1:
            return "pos"
        elif clas.mode == 0:
            return "neg"

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            if v == 'pos':
                v = 1
            elif v=='neg':
                v = 0
            votes.append(v)
        clas = scipy.stats.mstats.mode(votes)
        choice_votes = votes.count(clas.mode)
        conf = choice_votes / len(votes)
        return conf


def word_feats(words):
    return dict([(word, True) for word in words])


# # -- Load from pickle --
trainfeats_f = open("trainfeats.pickle", "rb")
trainfeats = pickle.load(trainfeats_f)
trainfeats_f.close()
testfeats_f = open("testfeats.pickle", "rb")
testfeats = pickle.load(testfeats_f)
testfeats_f.close()



# ## -- Load from pickle --
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
print 'NaiveBayes_Classifier Accuracy percent:', round((nltk.classify.accuracy(classifier, testfeats) * 100),2)
print 'NaiveBayes_Classifier ', classifier.show_most_informative_features(10)


# # -- Load from pickle --
classifier_f = open("MNB_classifier.pickle", "rb")
MNB_classifier = pickle.load(classifier_f)
classifier_f.close()
print 'MNB_classifier accuracy percent:', round((nltk.classify.accuracy(MNB_classifier, testfeats))*100,2)


# -- Load from pickle --
classifier_f = open("BernoulliNB_classifier.pickle", "rb")
BernoulliNB_classifier = pickle.load(classifier_f)
classifier_f.close()
print 'BernoulliNB_classifier accuracy percent:', round((nltk.classify.accuracy(BernoulliNB_classifier, testfeats))*100,2)


# -- Load from pickle --
classifier_f = open("SVC_classifier.pickle", "rb")
SVC_classifier = pickle.load(classifier_f)
classifier_f.close()
print 'SVC_classifier accuracy percent:'\
    , round((nltk.classify.accuracy(SVC_classifier, testfeats)) * 100,2)



# -- Load from pickle --
classifier_f = open("NuSVC_classifier.pickle", "rb")
NuSVC_classifier = pickle.load(classifier_f)
classifier_f.close()
print 'NuSVC_classifier accuracy percent:'\
    , round((nltk.classify.accuracy(NuSVC_classifier, testfeats)) * 100,2)
#
#
# # ----input

EULAdir = 'EULAcorpus/'
assert os.path.isdir(EULAdir)
for i in os.listdir(EULAdir):
    f = open(EULAdir+i, 'r')
    print "\n --- \n Testing with a", i, "input:\n --- \n"
    flines = f.read()
    words = flines.split()
    textfeature = word_feats(words)
    inputtest = set(textfeature)

    print 'NaiveBayesClassifier probability that it is a (neg)', \
        round((classifier.prob_classify(textfeature)).prob('neg'),2)
    print 'NaiveBayesClassifier probability that it is a(pos)', \
        round((classifier.prob_classify(textfeature)).prob('pos'),2)

    print('-' * 15)
    print 'NaiveBayesClassifier:', classifier.classify(textfeature)
    print 'MNB_classifier:', MNB_classifier.classify(textfeature)
    print 'BernoulliNB_classifier:', BernoulliNB_classifier.classify(textfeature)
    print 'SVC_classifier:', SVC_classifier.classify(textfeature)
    print 'NuSVC_classifier:', NuSVC_classifier.classify(textfeature)

    voted_classifier = VoteClassifier(classifier,
                                      SVC_classifier,
                                      NuSVC_classifier,
                                      MNB_classifier,
                                      BernoulliNB_classifier)

    print'\nMost voted classification:', voted_classifier.classify(textfeature),\
        '\nConfidence:',round(voted_classifier.confidence(textfeature)*100,2)
    print 'voted_classifier accuracy percent:', round((nltk.classify.accuracy(voted_classifier, testfeats)) * 100,2)
2
print('-' * 15)
# http://stackoverflow.com/questions/20827741/nltk-naivebayesclassifier-training-for-sentiment-analysis
#
#
# Refrences
# https://pythonprogramming.net/combine-classifier-algorithms-nltk-tutorial/
# https://pythonprogramming.net/pickle-classifier-save-nltk-tutorial/
# http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
# http://www.nltk.org/howto/classify.html
# http://stackoverflow.com/questions/20827741/nltk-naivebayesclassifier-training-for-sentiment-analysis
