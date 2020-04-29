#!/usr/bin/python3

#  Created by MikBac on 2020

def getNGramTuples(words, n):
	terms = []
	for ngram in range(2, n + 1):
		for i in range(len(words) - (ngram - 1)):
			gram = ()
			for j in range(ngram):
				gram = gram + (words[i + j],)
			terms.append(gram)
	terms += words

	return terms


def getNGramList(words, n):
	terms = []
	for ngram in range(2, n + 1):
		for i in range(len(words) - (ngram - 1)):
			gram = []
			for j in range(ngram):
				gram.append(words[i + j], )
			terms.append(gram)
	terms += words

	return terms
