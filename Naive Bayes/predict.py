#!/usr/bin/python3
import json
import math
import pickle
import sys

sys.path.append(sys.path[0] + "/..")
from Normalization.ExperimentalNormalization import getExperimentalNormalization

with open('./settings.json') as f:
	settings = json.load(f)

model = pickle.load(open("model.pkl", "rb"))
pVariantOne, pVariantTwo, variantOne_count, variantTwo_count, variantOne_words_total, variantTwo_words_total, vocabulary_size = model

for line in sys.stdin:
	document = line.strip().split('\t')[0]
	terms = getExperimentalNormalization(document, 3)

	log_prob_variantTwo = math.log(pVariantTwo)
	log_prob_variantOne = math.log(pVariantOne)

	for term in terms:

		if term not in variantTwo_count:
			variantTwo_count[term] = 0
		if term not in variantOne_count:
			variantOne_count[term] = 0

		log_prob_variantTwo += math.log((variantTwo_count[term] + 1) / (variantTwo_words_total + vocabulary_size))
		log_prob_variantOne += math.log((variantOne_count[term] + 1) / (variantOne_words_total + vocabulary_size))

	if log_prob_variantTwo > log_prob_variantOne:
		print(settings['variantTwo'])
	else:
		print(settings['variantOne'])
