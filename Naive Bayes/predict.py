#!/usr/bin/python3

import math
import pickle
import sys

from Normalization.ExperimentalNormalization import getExperimentalNormalization

model = pickle.load(open("model.pkl", "rb"))

pskeptic, vocabulary_size, skeptic_words_total, paranormal_words_total, skeptic_count, paranormal_count = model

for line in sys.stdin:
	document = line.strip().split('\t')[0]
	terms = getExperimentalNormalization(document, 3)

	log_prob_skeptic = math.log(pskeptic)
	log_prob_paranormal = math.log(1 - pskeptic)

	for term in terms:

		if term not in skeptic_count:
			skeptic_count[term] = 0
		if term not in paranormal_count:
			paranormal_count[term] = 0

		log_prob_skeptic += math.log((skeptic_count[term] + 1) / (skeptic_words_total + vocabulary_size))
		log_prob_paranormal += math.log((paranormal_count[term] + 1) / (paranormal_words_total + vocabulary_size))

	if log_prob_skeptic > log_prob_paranormal:
		print('S')
	else:
		print('P')
