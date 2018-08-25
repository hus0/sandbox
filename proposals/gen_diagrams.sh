#!/bin/bash

for i in `ls *.plantuml`
do
    plantuml $i
done
