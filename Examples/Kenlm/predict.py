#!/usr/bin/env python

#  Created by MikBac on 2020

import os
import sys

import kenlm

LM = os.path.join(os.path.dirname(__file__), 'train', 'dataIn.arpa')
model = kenlm.LanguageModel(LM)

for line in sys.stdin:

	sentence = line.strip()
	sentence = sentence.lower()


	def score(s):
		return sum(prob for prob, _, _ in model.full_scores(s))


	assert (abs(score(sentence) - model.score(sentence)) < 1e-3)

	words = ['<s>'] + sentence.split() + ['</s>']
	ans = []
	for i, (prob, length, oov) in enumerate(model.full_scores(sentence)):
		if prob < -6.5 and length == 1:
			for ii in range(length):
				ans.append(str(i + 2 - length + ii))

		if prob < -6.5 and length == 2 and (i + 2 - length) != 0:
			for ii in range(length):
				ans.append(str(i + 2 - length + ii))

		if prob < -6.5 and length == 3 and (i + 2 - length) != 0:
			for ii in range(length):
				ans.append(str(i + 2 - length + ii))

	state = kenlm.State()
	state2 = kenlm.State()

	model.BeginSentenceWrite(state)
	accum = 0.0
	accum += model.BaseScore(state, 'a', state2)
	accum += model.BaseScore(state2, 'sentence', state)

	assert (abs(accum - model.score("a sentence", eos=False)) < 1e-3)
	accum += model.BaseScore(state, "</s>", state2)
	assert (abs(accum - model.score("a sentence")) < 1e-3)
	print(' '.join(ans))
