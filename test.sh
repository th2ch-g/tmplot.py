#!/bin/bash
set -e

cat data/sample.txt | uv run python3 -m tmplot plot -f - -o test1.png
cat data/sample.txt | uv run python3 -m tmplot scatter -f - -o test2.png
cat data/sample.txt | awk '{print $2}' | uv run python3 -m tmplot hist -f - -o test3.png
cat data/sample.xvg | uv run python3 -m tmplot plot -f - -o test1_2.png

uv run python3 -m tmplot cat plot -f data/sample.txt data/sample.xvg -o test4.png
uv run python3 -m tmplot cat scatter -f data/sample.txt data/sample.xvg -o test5.png
uv run python3 -m tmplot cat hist -f data/sample.txt data/sample.xvg -o test6.png

cat data/sample2.txt | uv run python3 -m tmplot twin plot -f - -o test7.png
cat data/sample2.txt | uv run python3 -m tmplot twin scatter -f - -o test8.png
