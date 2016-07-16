# Program that cleans venmo text file
import simplejson as sj
import sys
import os
import urllib
txt = urllib.urlopen(
    "https://raw.githubusercontent.com/InsightDataScience/coding-challenge/master/data-gen/venmo-trans.txt").read()

input_file = open(sys.argv[1])

for line in input_file:
    try: # extraction of timestamp, tweet text from json. If a unicode tweet is found triggers exception
        json = sj.loads(line.strip())

input_file = open(sys.argv[1])