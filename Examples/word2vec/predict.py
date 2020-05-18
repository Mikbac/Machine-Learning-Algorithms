# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

from __future__ import division

import collections
import pickle
import sys
from gensim.models import Word2Vec
from itertools import islice

from SimpleNormalization import getNormalization


def take(n, iterable):
	return list(islice(iterable, n))

def main():
	model = Word2Vec.load('./data/model.bin')
	modelPkl = pickle.load(open("./data/model.pkl", "rb"))
	fieldsDict = modelPkl
	for line in sys.stdin:
		stats = {}
		skeptic = 0
		paranormal = 0
		if len(line) != 0:
			line = line.strip()
			fields = line.split('\t')
		else:
			fields = ['empty']
		label = fields[0].strip()
		label = getNormalization(label)
		round = 0
		for key in fieldsDict:
			if round == 10000:
				break
			try:
				similiarAns = model.wv.n_similarity(getNormalization(key), label)
			except:
				similiarAns = 0.4
				stats[similiarAns] = '0'
				similiarAns = 0.6
				stats[similiarAns] = '1'
				break
			stats[similiarAns] = fieldsDict[key]
			round += 1

		sortedStats = collections.OrderedDict(sorted(stats.items(), reverse=True))
		k = 0

		for i in sortedStats:
			if k == 1000:
				break
			if sortedStats[i] == '0':
				skeptic += 1
			else:
				paranormal += 1
			k += 1
		if (paranormal / (skeptic + paranormal)) <= 0.15:
			print('0.15')
		elif (paranormal / (skeptic + paranormal)) >= 0.85:
			print('0.85')
		else:
			print(paranormal / (skeptic + paranormal))


if __name__ == '__main__':
	main()
