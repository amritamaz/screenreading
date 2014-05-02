#!/bin/bash

echo "Integrating all TXTs to all.txt"

cat corpus/*.txt >> corpus/all.txt
#convert encoding
echo "Converting to Ascii"
iconv -f utf8 -t US-ASCII corpus/all.txt corpus/all_ascii.txt
