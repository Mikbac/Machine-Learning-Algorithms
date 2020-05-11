#!/bin/bash

name="dos2unix"

if [ $? -ne 0 ]; then
  echo $name "is not installed"
  sudo apt-get update
  sudo apt-get install $name
else
  echo $name "is installed"
fi

dos2unix ./Naive\ Bayes\ -\ binary/NaiveBayes.sh