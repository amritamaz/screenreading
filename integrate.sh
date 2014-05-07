#!/bin/bash

echo "Integrating all TXTs to all.txt"

rm corpus/all.txt > /dev/null
cat corpus/*.txt > corpus/all.txt
#convert encoding
echo "Converting to Ascii"
iconv -cs -f utf8 -t US-ASCII corpus/all.txt > corpus/all_ascii.txt
