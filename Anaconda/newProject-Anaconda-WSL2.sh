#!/bin/bash

# Created by MikBac on 2020

conda create --name projectName &&

conda activate tau &&

conda install python &&

# https://pytorch.org/get-started/locally/
#
# pytorch build: stable
# your os: linux
# Package: conda
# Language: Python
# CUDA: CPU -> none; GPU nvidia -> 11.0

conda install pytorch torchvision torchaudio cpuonly -c pytorch &&

conda install pip numpy jupyter ipython scikit-learn pandas
