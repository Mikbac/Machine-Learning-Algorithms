#!/bin/bash
(dos2unix * && ./NaiveBayes.sh) || (sudo apt-get install dos2unix && dos2unix * && ./NaiveBayes.sh);