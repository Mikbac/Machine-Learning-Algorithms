#!/bin/bash

pathToTrainDataSet="./../Data/ParanormalOrSkeptic/train/in.tsv"
pathToTrainExpectedSet="./../Data/ParanormalOrSkeptic/train/expected.tsv"
pathToPredictSet="./../Data/ParanormalOrSkeptic/test/in.tsv"

echo "Naive Bayes for binary classification started for:"

cat ./settings.json

cat $pathToTrainDataSet | paste $pathToTrainExpectedSet - | python3 ./train.py && cat $pathToPredictSet | python3 ./predict.py >./out.tsv

echo "Naive Bayes for binary classification ended"
