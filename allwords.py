import nltk, re, pprint
from nltk.corpus import stopwords
from nltk import FreqDist
import matplotlib

# open all.txt into all
#all = open('corpus/hermeneutics.txt').read()
all = open('corpus/all.txt').read()

# normalize our corpus
tokens = nltk.word_tokenize(all)

# lowercase
words = [w.lower() for w in tokens]

# remove stopwords
words = [w for w in words if not w in stopwords.words('english')]

# remove 1 and 2 letter words
words = [w for w in words if len(w)!=1]
words = [w for w in words if len(w)!=2]

# remove unicode characters
words = [w.decode('unicode_escape').encode('ascii','ignore') for w in words]
vocab = sorted(set(words))

# let's find the most frequent words
fdist1 = FreqDist(words)
fdist1.plot(50,cumulative=True)


