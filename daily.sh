#!/bin/bash

set -euo pipefail

TODAY=$(date +"%Y-%m-%d")

function log() {
	printf "original wordle:\n"
	./eldrow.py
	printf "nyt wordle:\n"
	./eldrow.py --nyt
}

if grep -q "${TODAY}" "./wordle-dates.txt"; then
	log
else
	echo "${TODAY}" >> ./wordle-dates.txt
	log
fi

