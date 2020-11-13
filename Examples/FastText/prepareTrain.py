#!/usr/bin/python

#  Created by MikBac on 2020

import sys

from SimpleNormalization import getNormalization

for line in sys.stdin:
	line = line.strip()
	line = line.strip()
	fields = line.split('\t')
	print('__label__' + fields[0][:4] + ' ' + getNormalization(fields[len(fields) - 1]))
