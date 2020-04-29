#!/usr/bin/python3

import pickle
import sys

from Normalization.ExperimentalNormalization import getExperimentalNormalization


def train():
	documents_total = 0
	skeptic_documents_total = 0
	paranormal_documents_total = 0

	vocabulary = set()

	skeptic_words_total = 0
	paranormal_words_total = 0

	skeptic_count = {}
	paranormal_count = {}

	for line in sys.stdin:

		line = line.strip()
		fields = line.split('\t')
		label = fields[0].strip()
		document = fields[1]
		terms = getExperimentalNormalization(document, 3)
		for t in terms:
			vocabulary.add(t)

		documents_total += 1

		if label == 'S':
			skeptic_documents_total += 1
			skeptic_words_total += len(terms)
			for term in terms:
				if term in skeptic_count:
					skeptic_count[term] += 1
				else:
					skeptic_count[term] = 1
		else:
			paranormal_documents_total += 1
			paranormal_words_total += len(terms)
			for term in terms:
				if term in paranormal_count:
					paranormal_count[term] += 1
				else:
					paranormal_count[term] = 1

	pskeptic = skeptic_documents_total / documents_total
	vocabulary_size = len(vocabulary)

	model = (pskeptic,
	         vocabulary_size,
	         skeptic_words_total,
	         paranormal_words_total,
	         skeptic_count,
	         paranormal_count)

	pickle.dump(model, open("model.pkl", "wb"))

	print(paranormal_count)


train()
