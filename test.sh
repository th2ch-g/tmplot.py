#!/bin/bash
set -e

cat data/sample.txt | pipenv run tmplot plot -f - -o test1.png
cat data/sample.txt | pipenv run tmplot scatter -f - -o test2.png
cat data/sample.txt | awk '{print $2}' | pipenv run tmplot hist -f - -o test3.png
cat data/sample.xvg | pipenv run tmplot plot -f - -o test1_2.png

pipenv run tmplot cat plot -f data/sample.txt data/sample.xvg -o test4.png
pipenv run tmplot cat scatter -f data/sample.txt data/sample.xvg -o test5.png
pipenv run tmplot cat hist -f data/sample.txt data/sample.xvg -o test6.png

cat data/sample2.txt | pipenv run tmplot twin plot -f - -o test7.png
cat data/sample2.txt | pipenv run tmplot twin scatter -f - -o test8.png
