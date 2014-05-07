import nltk, re, pprint
from nltk.corpus import stopwords
from nltk import FreqDist
import matplotlib

# open all.txt into all
#all = open('corpus/hermeneutics.txt').read()

# make an array with all the file names
from os import listdir
from os.path import isfile, join
mypath = './corpus/.'
onlyfiles=[ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
filewords = []
for f in onlyfiles:
    frequencies = []
    print(f+', '+str(onlyfiles.index(f)+1)+'/'+str(len(onlyfiles)))
    if f=='.DS_Store' or f=='all.txt' or f=='all_ascii.txt':
	continue
    current = open('corpus/'+f).read()
    tokens = nltk.word_tokenize(current)
    words = [w.lower() for w in tokens]
    words = [w for w in words if not w in stopwords.words('english')]
    words = [w for w in words if (len(w) != 1 and len(w) != 2)]
    fdist1 = FreqDist(words)
    fdist_words = fdist1.keys()
    for i in range(30):
	frequencies.append([fdist_words[i],fdist1[fdist_words[i]]])
    filewords.append([f,frequencies])

print(filewords)
print('done!')

import operator
most_freqs_dict = {}
most_freqs_sorted = []
def most_frequent():
    for f in filewords:
	fname = f[0]
	freqs = f[1]
	for fr in freqs:
	    if fr[0] not in most_freqs_dict:
		most_freqs_dict[fr[0]] = 1
	    else:
		most_freqs_dict[fr[0]] += 1
    print(most_freqs_sorted)

most_frequent()
most_freqs_sorted = sorted(most_freqs_dict.iteritems(), key=operator.itemgetter(1))
print('really done!')
'''
all = open('corpus/all_ascii.txt').read()

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
'''

