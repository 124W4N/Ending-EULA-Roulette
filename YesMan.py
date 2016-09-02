# Yes-Man TOOL.
# Run it after Saving (Step 1)

import win32gui
import win32con
import os
import pickle
import scipy
from nltk.classify import ClassifierI


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = [ ]
        for c in self._classifiers:
            v = c.classify(features)
            if v == "pos":
                v = 1
            elif v == 'neg':
                v = 0
            votes.append(v)
        clas = scipy.stats.mstats.mode(votes)
        if clas.mode == 1:
            return "pos"
        elif clas.mode == 0:
            return "neg"

    def confidence(self, features):
        votes = [ ]
        for c in self._classifiers:
            v = c.classify(features)
            if v == 'pos':
                v = 1
            elif v == 'neg':
                v = 0
            votes.append(v)
        clas = scipy.stats.mstats.mode(votes)
        choice_votes = votes.count(clas.mode)
        conf = choice_votes / len(votes)
        return conf


def word_feats(words):
    return dict([ (word, True) for word in words ])


# ## -- Load from pickle --
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

# # -- Load from pickle --
classifier_f = open("MNB_classifier.pickle", "rb")
MNB_classifier = pickle.load(classifier_f)
classifier_f.close()

# -- Load from pickle --
classifier_f = open("BernoulliNB_classifier.pickle", "rb")
BernoulliNB_classifier = pickle.load(classifier_f)
classifier_f.close()


# -- Load from pickle --
classifier_f = open("SVC_classifier.pickle", "rb")
SVC_classifier = pickle.load(classifier_f)
classifier_f.close()

# -- Load from pickle --
classifier_f = open("NuSVC_classifier.pickle", "rb")
NuSVC_classifier = pickle.load(classifier_f)
classifier_f.close()

childHandle = [ ]
EULAHandle = [ ]
EULAdir = 'EULAcorpus/'
filename = "1"


def CallBack(hwnd, lParam):
    childHandle.append(hwnd)


def contentExtractor(hwnd):
    for i in childHandle:
        bufferSize = 1 + win32gui.SendMessage(i, win32con.WM_GETTEXTLENGTH, 0, 0)
        buffer = win32gui.PyMakeBuffer(bufferSize)
        win32gui.SendMessage(i, win32con.WM_GETTEXT, bufferSize, buffer)
        if bufferSize > 500:
            agreement = (buffer[ :bufferSize ])
            # Normalize
            import re
            from nltk.corpus import stopwords
            letters_only = re.sub("[^a-zA-Z0-9]", " ", agreement)
            words = letters_only.lower().split()
            stops = set(stopwords.words("english"))
            meaningful_words = [ w for w in words if not w in stops ]
            KK = (" ".join(meaningful_words))
            # print the agreement to a file
            if not os.path.isdir(EULAdir):
                os.mkdir(EULAdir)

            if os.path.isfile(EULAdir + filename + '.txt'):
                print "duplicated names"

            MyFile = open(EULAdir + filename + '.txt', 'w')
            MyFile.write(KK)
            MyFile.close()
            EULAHandle.append(True)
            return True
    return False


def ClickButton(hwnd, lParam):
    # Run on the pyautogui internal shell with desired button click location and as such the higher level of coding and optimization will be required
    import pyautogui
    #  pyautogui.click(10, 5)
    # or press the enter keyboard button if the button is already active
    pyautogui.press('enter')


def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        # 1 Checking against possible EULA title
        Title = (win32gui.GetWindowText(hwnd)).lower()
        if "setup" in Title or "license" in Title or "agreement" in Title:
            print (Title)
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            try:
                win32gui.SetForegroundWindow(hwnd)
            except:
                pass

            try:
                win32gui.EnumChildWindows(hwnd, CallBack, None)
            except:
                print "No children in the window found"

            # 2 GRAP THE CONTENT
            # win32gui.EnumChildWindows(hwnd, GrapContent, None)
            contentExtractor(hwnd)
            # 3 Checking against Agreeing button
            for i in range(len(childHandle)):
                Button1=(win32gui.GetWindowText(childHandle[ i ])).lower()
                if "accept" in Button1 or "next" in Button1 or "install" in Button1 or "i agree" in Button1 or "i &agree" in Button1 or "i &accept the agreement" in Button1:

                    # 4 analyzing the text
                    f = open(EULAdir + filename + '.txt', 'r')
                    srt = f.read()
                    f.close()

                    words = srt.split()
                    textfeature = word_feats(words)
                    voted_classifier = VoteClassifier(classifier,
                                      SVC_classifier,
                                      NuSVC_classifier,
                                      MNB_classifier,
                                      BernoulliNB_classifier)
                    if voted_classifier.classify(textfeature) == "pos":
                        # For 'pos' classification, only accept the ones with high confidence to ensure that it is really a EULA
                        if round(voted_classifier.confidence(textfeature) * 100, 2) >= 70.00:
                            # 5 CLICK THE BUTTON
                            ClickButton(hwnd, None)
                            # Reset for the next window
                            for x in childHandle:
                                childHandle.remove(x)

                            print 'voted pos'
                    elif voted_classifier.classify(textfeature) == "neg":
                        for x in childHandle:
                            childHandle.remove(x)

                        print 'voted neg'




            for x in childHandle:
                childHandle.remove(x)

win32gui.EnumWindows(enumHandler, None)
