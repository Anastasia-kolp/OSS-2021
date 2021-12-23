#!/bin/bash

find ~ -name "*.txt" > /tmp/2_5.txt 2>/dev/null
cat /tmp/2_5.txt | wc -l
du -h /tmp/2_5.txt | cut -f1
rm /tmp/2_5.txt
