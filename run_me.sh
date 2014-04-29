#!/bin/bash

echo "Converting PDF to TXT..."
SECTIONS="*/*.pdf"

for f in $SECTIONS
do
    q=$(echo $f | sed 's/ /\\ /g')
    echo "pdftotext $q ${q%.pdf}.txt"
    p="pdftotext $q ${q%.pdf}.txt"
    eval $p
done

