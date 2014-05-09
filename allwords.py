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
		print('handling '+fname)
		freqs = f[1]
		for fr in freqs:
			if fr[0] not in most_freqs_dict:
				most_freqs_dict[fr[0]] = 1
			else:
				most_freqs_dict[fr[0]] += 1
		print(most_freqs_dict)

	most_frequent()
	most_freqs_sorted = sorted(most_freqs_dict.iteritems(), key=operator.itemgetter(1))
	most_freqs_sorted.reverse()
	for word in most_freqs_sorted:
		percent = word[1]/32.0
		most_freqs_sorted[most_freqs_sorted.index(word)] = (word[0], percent)

keywords = ['alphabet', 'village', 'universal', 'colophon', 'metadata', 'content', 'writing', 'interface', 'text', 'reading', 'book', 'type']

def keywords():
mypath = './corpus/.'
onlyfiles=[ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
filewords = []
keyword_data = {}
for f in onlyfiles:
	frequencies = []
	print(f+', '+str(onlyfiles.index(f)+1)+'/'+str(len(onlyfiles)))
	if 'week' not in f:
		continue
	current = open('corpus/'+f).read()
	tokens = nltk.word_tokenize(current)
	words = [w.lower() for w in tokens]
	words = [w for w in words if not w in stopwords.words('english')]
	words = [w for w in words if (len(w) != 1 and len(w) != 2)]
	fdist1 = FreqDist(words)
	fdist_words = fdist1.keys()
	for i in range(len(fdist_words)):
		frequencies.append([fdist_words[i],fdist1[fdist_words[i]]])
	filewords.append([f,frequencies])
	for week in filewords:
		frqz = week[1]
		for frq in frqz:
			if frq[0] in keywords:
				if frq[0] not in keyword_data.keys(): # then doesnt have an entry
					keyword_data[frq[0]] = []
				keyword_data[frq[0]].append([f.split('.')[0],float(frq[1])/len(frqz)])
				print([frq[0],frqz.index(frq),f.split('.')[0],float(frq[1])/len(frqz)])

	new_keyword_data = {}
	for ky in keyword_data:
		keyword_freq_dict = {}
		for item in keyword_data[ky]:
			if item[0] not in keyword_freq_dict.keys():
				keyword_freq_dict[item[0]] = item[1]
			else:
				keyword_freq_dict[item[0]] += item[1]
		keyword_data[ky] = keyword_freq_dict

for ky in keyword_data:
	for item in keyword_data[ky]:
		keyword_data[ky][item] = keyword_data[ky][item] / max(keyword_data[ky].values())

for ky in keyword_data:
	print(ky)
	for item in keyword_data[ky]:
		print('\t'+item+"\t%.6f" % keyword_data[ky][item])

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

