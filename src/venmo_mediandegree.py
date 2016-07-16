import sys
import json
import time
import itertools
import datetime
import simplejson as sj
import sys
import os
import urllib
txt = urllib.urlopen(
    "https://raw.githubusercontent.com/InsightDataScience/coding-challenge/master/data-gen/venmo-trans.txt").read()

input_file = o

for line in input_file:
    try: # extraction of timestamp, tweet text from json. If a unicode tweet is found triggers exception
        json = sj.loads(line.strip())