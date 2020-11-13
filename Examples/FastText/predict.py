# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

import fasttext
import sys
from SimpleNormalization import getNormalization

model = fasttext.load_model("./model.bin")


for line in sys.stdin:
	line = line.strip()
	line = line.strip()

	k = 200
	top = 0
	bot = 0
	ans = model.predict(getNormalization(line.decode('utf-8')), k=k)
	for i in range(k):
		top += int(ans[0][i].replace('__label__', '')) * ans[1][i]
		bot += ans[1][i]
	print(top/bot)

