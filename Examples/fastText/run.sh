#!/bin/bash

#  Created by MikBac on 2020

xzcat ./train/train.tsv.xz | python prepareTrain.py >./train/data.tsv

python train.py

cat ./test/in.tsv | python predict.py > ./test-A/out.tsv
