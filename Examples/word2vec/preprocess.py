# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

import pickle
import sys

from SimpleNormalization import getNormalization


def main():
	fieldsDict = {}
	for line in sys.stdin:
		fields = line.split('\t')
		label = fields[1].strip()
		label = ' '.join(getNormalization(label))
		if len(label) != 0:
			print(label)
			fieldsDict[label] = fields[0].replace('\r', '')
		else:
			print("empty")
			fieldsDict["empty"] = fields[0].replace('\r', '')

	model = (fieldsDict)
	pickle.dump(model, open("./train/model.pkl", "wb"), 0)


if __name__ == '__main__':
	main()
