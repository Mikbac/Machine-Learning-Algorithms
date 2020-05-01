#!/usr/bin/python3
import json
import pickle
import sys

sys.path.append(sys.path[0] + "/..")
from Normalization.ExperimentalNormalization import getExperimentalNormalization


def train():
	with open('./settings.json') as f:
		settings = json.load(f)

	documents_total = 0
	vocabulary = set()

	variantOne_documents_total = 0
	variantTwo_documents_total = 0

	variantOne_words_total = 0
	variantTwo_words_total = 0

	variantOne_count = {}
	variantTwo_count = {}

	for line in sys.stdin:

		line = line.strip()
		fields = line.split('\t')
		label = fields[0].strip()
		document = fields[1]
		terms = getExperimentalNormalization(document, 3)
		for t in terms:
			vocabulary.add(t)

		documents_total += 1

		if label == settings['variantOne']:
			variantOne_documents_total += 1
			variantOne_words_total += len(terms)
			for term in terms:
				if term in variantOne_count:
					variantOne_count[term] += 1
				else:
					variantOne_count[term] = 1
		elif label == settings['variantTwo']:
			variantTwo_documents_total += 1
			variantTwo_words_total += len(terms)
			for term in terms:
				if term in variantTwo_count:
					variantTwo_count[term] += 1
				else:
					variantTwo_count[term] = 1

	pVariantOne = variantOne_documents_total / documents_total
	pVariantTwo = variantTwo_documents_total / documents_total
	vocabulary_size = len(vocabulary)

	model = (pVariantOne,
	         pVariantTwo,
	         variantOne_count,
	         variantTwo_count,
	         variantOne_words_total,
	         variantTwo_words_total,
	         vocabulary_size)

	pickle.dump(model, open("model.pkl", "wb"))


train()
