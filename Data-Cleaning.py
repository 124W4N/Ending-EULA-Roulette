import re, os
from nltk.corpus import stopwords

# Initial prepossessing for neg
# s = ['noteula1','noteula2','noteula3','noteula4','noteula5','noteula6','noteula7','noteula8','noteula9','noteula10','noteula11','noteula12','noteula13','noteula14','noteula15']

# s=['16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42']
#
# DIR = 'DatasetCorpus/neg/'
# for i in os.listdir(DIR):
#     f = open(DIR+i, 'r')
#     flines = f.read()
#     #
#     # 2. Remove non-letters
#
#     letters_only = re.sub("[^a-zA-Z0-9]",  # The pattern to search for
#                           " ",  # The pattern to replace it with
#                           flines)  # The text to search
#
#     # 3. Convert to lower case, split into individual words
#     words = letters_only.lower().split()
#     #
#     # 4. In Python, searching a set is much faster than searching
#     #   a list, so convert the stop words to a set
#     # stopword-removal includes the words like 'and', 'or', 'not' gets removed
#     stops = set(stopwords.words("english"))
#     #
#     # 5. Remove stop words
#     meaningful_words = [w for w in words if not w in stops]
#     #
#     # 6. Join the words back into one string separated by space,
#     # and return the result.
#     str=(" ".join(meaningful_words))
#
#     f = open(DIR+i, 'w')
#     f.writelines(str)
#     f.close()

# # Initial prepossessing for pos
# #
# # # s = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
# # s=['21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42']
DIR = 'DatasetCorpus/pos/'
for i in os.listdir(DIR):
    f = open(DIR+i, 'r')
    flines = f.read()

    # 2. Remove non-letters
    letters_only = re.sub("[^a-zA-Z0-9]",  # The pattern to search for
                          " ",  # The pattern to replace it with
                          flines)  # The text to search

    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))
    #
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]
    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    str=(" ".join(meaningful_words))

    f = open(DIR+i, 'w')
    f.writelines(str)
    f.close()

#

#
#
# # https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words
#
#
#
# f = open('EULAcorpus/randomtext.txt', 'r')
# flines = f.read()
#
# # 2. Remove non-letters
# letters_only = re.sub("[^a-zA-Z0-9]",  # The pattern to search for
#                       " ",  # The pattern to replace it with
#                       flines)  # The text to search
#
# # 3. Convert to lower case, split into individual words
# words = letters_only.lower().split()
# #
# # 4. In Python, searching a set is much faster than searching
# #   a list, so convert the stop words to a set
# stops = set(stopwords.words("english"))
# #
# # 5. Remove stop words
# meaningful_words = [w for w in words if not w in stops]
# #
# # 6. Join the words back into one string separated by space,
# # and return the result.
# str = (" ".join(meaningful_words))
#
# f = open('EULACorpus/randomtext.txt', 'w')
# f.writelines(str)
# f.close()
