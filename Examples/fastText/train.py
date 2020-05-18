#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Created by MikBac on 2020

import fasttext

model = fasttext.train_supervised(input="train/data.tsv", lr=1.0, epoch=25, wordNgrams=3)

model.save_model("model.bin")
