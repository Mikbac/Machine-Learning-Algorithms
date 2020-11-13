# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

import sys

for line in sys.stdin:
	lines = line.split(' ||| ')

	print(lines[1].strip())
