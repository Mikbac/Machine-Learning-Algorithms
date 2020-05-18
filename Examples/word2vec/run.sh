#!/bin/bash

#  Created by MikBac on 2020

xzcat ./train/in.tsv.xz > ./train/in.tsv
xzcat ./test/in.tsv.xz > ./test-A/in.tsv

paste ./train/expected.tsv ./train/in.tsv > ./train/data.tsv

cat ./train/data.tsv | python3 preprocess.py > ./train/preprocessed_data.tsv

python3 train.py

#dos2unix ./test-A/in.tsv
#dos2unix ./dev-0/in.tsv

cat ./test/in.tsv | python3 predict.py > ./test/out.tsv
