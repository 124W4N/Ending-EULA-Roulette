# Validating ACCURACY using Cross-Validation
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
import nltk
from nltk.classify import ClassifierI
from sklearn import cross_validation

# # -- Load from pickle --
trainfeats_f = open("trainfeats.pickle", "rb")
trainfeats = pickle.load(trainfeats_f)
trainfeats_f.close()
testfeats_f = open("testfeats.pickle", "rb")
testfeats = pickle.load(testfeats_f)
testfeats_f.close()
allfeats=trainfeats+testfeats

class validation(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    def crossValid(self):
        cv = cross_validation.KFold(len(allfeats), n_folds=10, shuffle=True, random_state=None)
        for c in self._classifiers:
            for traincv, testcv in cv:
                    # print c
                    classifier = c.train(trainfeats[traincv[0]:traincv[len(traincv)-1]])
                    num=(nltk.classify.util.accuracy(classifier, testfeats[testcv[0]:testcv[len(testcv)-1]]))*100
                    accuracy =+ num
                    print 'accuracy:', num
                # find mean accuracy over all rounds
            average=accuracy/10
            print 'average accuracy:', average
            print('-' * 15)


v=validation(nltk.NaiveBayesClassifier,
           SklearnClassifier(MultinomialNB()),
            SklearnClassifier(BernoulliNB()),
           SklearnClassifier(NuSVC(probability=True)),
           SklearnClassifier(SVC(probability=True)))

v.crossValid()

