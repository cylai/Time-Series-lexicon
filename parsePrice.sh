#!/bin/bash

cat ${1}Price.txt | grep ^$2 -A1 -B1 | awk '{print $1 "\t" $2}' > ./SPindex/${2}temp.txt

./date.py $2

mv ${2}.txt ./SPindex
rm ./SPindex/${2}temp.txt

cat ./SPindex/${2}.txt | awk '{print $2}' > ./SPindex/${1}${2}.txt

rm ./SPindex/${2}.txt





