#!/bin/bash

for i in `ls *.txt`
do
    plantuml $i
done
