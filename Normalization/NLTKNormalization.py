#!/usr/bin/python3

#  Created by MikBac on 2020

import unicodedata

try:
	from .NGram.NGram import getNGramTuples
except:
	from NGram.NGram import getNGramTuples
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, WhitespaceTokenizer

stop_words = set(stopwords.words('english'))
blankline_tokenizer = WhitespaceTokenizer()
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def getNLTKNormalization(d, ngram=1):
	d = unicodedata.normalize('NFKD', d).encode('ascii', 'ignore').decode('utf-8', 'ignore')

	words = word_tokenize(d)

	words = [word for word in words if word.isalpha()]

	words = [i for i in words if not i in stop_words]

	for word in words:
		blankline_tokenizer.tokenize(word)

	words = [word for word in words if word.isalpha()]
	words = [word.lower() for word in words]
	words = [word for word in words if not word in stopwords.words("english")]
	words = [lemmatizer.lemmatize(word, pos="v") for word in words]
	words = [lemmatizer.lemmatize(word, pos="n") for word in words]
	words = [stemmer.stem(word) for word in words]

	words = getNGramTuples(words, ngram)

	return words
