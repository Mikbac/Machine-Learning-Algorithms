#!/usr/bin/python3

import re
import string

import unicodedata
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, WhitespaceTokenizer

stop_words = set(stopwords.words('english'))


def getExperimentalNormalization(d):
	d = unicodedata.normalize('NFKD', d).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	blankline_tokenizer = WhitespaceTokenizer()
	stemmer = PorterStemmer()
	lemmatizer = WordNetLemmatizer()

	d = d.lower()

	d = d.strip()

	d = d.replace('0', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ')
	d = d.replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ')

	d = d.replace(' zero ', ' ').replace(' one ', ' ').replace(' two ', ' ').replace(' three ', ' ').replace(' four ',
	                                                                                                         ' ')
	d = d.replace(' five ', ' ').replace(' six ', ' ').replace(' seven ', ' ').replace(' eight ', ' ').replace(' nine ',
	                                                                                                           ' ')

	d = d.replace(' ten ', ' ').replace(' eleven ', ' ').replace(' twelve ', ' ').replace(' thirteen ', ' ').replace(
		' fourteen ', ' ').replace(' fifteen ', ' ')
	d = d.replace(' sixteen ', ' ').replace(' seventeen ', ' ').replace(' eighteen ', ' ').replace(' nineteen ', ' ')

	d = d.replace(':', ' ').replace('\'', ' ').replace('^', ' ').replace('.', ' ').replace('*', ' ').replace('\"', ' ')
	d = d.replace(' \' ', ' ').replace('\r', ' ').replace('\s', ' ').replace('\t', ' ').replace('\n', ' ').replace(
		'\\n', ' ')
	d = d.replace('`', ' ').replace('~', ' ').replace('!', ' ').replace('@', ' ').replace('#', ' ').replace('$',
	                                                                                                        ' ').replace(
		'%', ' ').replace('^', ' ').replace('&', ' ')
	d = d.replace('*', ' ').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=', ' ').replace(';',
	                                                                                                        ' ').replace(
		'"', ' ').replace('|', ' ')
	d = d.replace('\\', ' ').replace(',', ' ').replace('.', ' ').replace('/', ' ').replace('?', ' ').replace('|', ' ')
	d = d.replace('{', ' ').replace('}', ' ').replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')',
	                                                                                                        ' ').replace(
		'<', ' ').replace('>', ' ')

	d = d.replace('http', '').replace('https', '').replace('youtube', '')

	d = re.sub('\\\\n', '', d)
	d = re.sub('[\[\(\)\]]', ' ', d)
	d = re.sub('this[\.\:]', 'this ', d)
	d = re.sub('https?://\S*', '', d)
	d = re.sub('[a-zA-Z]\.[a-zA-Z]', ' ', d)

	d = re.sub('   ', ' ', d)
	d = re.sub('  ', ' ', d)

	d = d.translate(str.maketrans('', '', string.punctuation))

	d = unicodedata.normalize('NFKD', d).encode('ascii', 'ignore').decode('utf-8', 'ignore')

	d = d.strip()

	d = ' '.join(d.split())

	words = word_tokenize(d)

	words = [word for word in words if word.isalpha()]

	words = [i for i in words if not i in stop_words]

	for word in words:
		blankline_tokenizer.tokenize(word)
		word = stemmer.stem(word)
		word = lemmatizer.lemmatize(word)

	words2 = [s for s in words if len(s) > 1]

	# round II
	words2 = [word for word in words2 if word.isalpha()]
	words2 = [word.lower() for word in words2]
	words2 = [word for word in words2 if not word in stopwords.words("english")]
	words2 = [lemmatizer.lemmatize(word, pos="v") for word in words2]
	words2 = [lemmatizer.lemmatize(word, pos="n") for word in words2]

	return words2
