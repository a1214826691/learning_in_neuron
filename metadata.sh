#!/bin/bash
#31268532，23761740，15703259，35036070，31761708

>metadata.csv

pmids=("31268532" "23761740" "15703259" "35036070" "31761708")

for pmid in "${pmids[@]}"
do
    python metadata.py "$pmid" &
done

wait

