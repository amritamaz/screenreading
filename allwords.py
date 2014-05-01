import nltk, re, pprint
from nltk.corpus import stopwords
from nltk import FreqDist
import matplotlib

# open all.txt into all
#all = open('corpus/hermeneutics.txt').read()
all = open('corpus/all.txt').read()

# normalize our corpus
tokens = nltk.word_tokenize(all)
words = [w.lower() for w in tokens]
words = [w for w in words if not w in stopwords.words('english')]
words = [w for w in words if len(w)!=1]
words = [w for w in words if len(w)!=2]

vocab = sorted(set(words))

# let's find the most frequent words
fdist1 = FreqDist(words)
fdist1.plot(50,cumulative=True)


