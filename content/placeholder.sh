#!/bin/bash

for s in s13 s14 s15 s16 s17 s18; do
    cd $s*
    for p in p01 p02 p03; do
        touch "${s}_${p}.md"
    done
    cd -
done
