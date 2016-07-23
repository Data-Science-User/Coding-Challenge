# Program that cleans venmo text file
import urllib
import json, sys, os, re, networkx, io
import pandas as pd
import requests
import datetime as dt
import itertools
from pprint import pprint
from collections import Counter
import random
import numpy as np

input_file = open(sys.argv[1])

txt = urllib.urlopen(
    "https://raw.githubusercontent.com/InsightDataScience/coding-challenge/master/data-gen/venmo-trans.txt").read()

for line in input_file:
    try: # extraction of timestamp, tweet text from json. If a unicode tweet is found triggers exception
        json = sj.loads(line.strip())
        Created_time = json['Created_time']
        Target = json['Target']
        Actor = json['Actor']

sys.argv = [w.replace('52801', '/Users/Chak/Documents/GitHub/Coding-Challenge/Venmo_input/Venmo.txt')
            .replace('52802', '/Users/Chak/Documents/GitHub/Coding-Challenge/Venmo_output/output1.txt')for w in sys.argv]

sys.argv = [w.replace('52802', '/Users/Chak/Documents/GitHub/Coding-Challenge/Venmo_output/output1.txt') for w in sys.argv]

sys.argv = [w.replace('\\','/').replace('C:',"") for w in sys.argv]

input_file = open(sys.argv[1])


import urllib, json
url = "https://raw.githubusercontent.com/chakwong87/Coding-Challenge/master/venmo_input/venmo.txt"
response = urllib.urlopen("https://raw.githubusercontent.com/chakwong87/Coding-Challenge/master/venmo_input/venmo.txt").read()
data = json.loads(response)
print data


data = []
with open("https://raw.githubusercontent.com/chakwong87/Coding-Challenge/master/venmo_input/venmo.txt") as f:
    for line in f:
        data.append(json.loads(line))

import json, requests
u = "http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?alt=json"
json.loads(requests.get(u).text) # <-- request + parse

url = "https://raw.githubusercontent.com/chakwong87/Coding-Challenge/master/venmo_input/venmo.txt"
json.loads(requests.get(url).text)


Created_time = {}
Target = {}
Actor = {}
json.dumps([Created_time, Target, Actor])
json.loads(json.dumps([Created_time, Target, Actor]))


venmo = pd.read_csv("https://raw.githubusercontent.com/InsightDataScience/coding-challenge/master/data-gen/venmo-trans.txt",
                names = ["Created_time", "Target", "Actor"])
venmo = venmo[['Actor', 'Target', 'Created_time']]
# Restructure file applicable for graphing
venmo['Created_time'] = venmo['Created_time'].map(lambda x: str(x)[18:-1])
# venmo['Created_time'] = venmo['Created_time'].replace({'T': ' '}, regex=True)
venmo['Target'] = venmo['Target'].map(lambda x: str(x)[12:-1])
venmo['Actor'] = venmo['Actor'].map(lambda x: str(x)[11:-2])
venmo["Created_time"] = pd.to_datetime(venmo["Created_time"], infer_datetime_format=True)

test = venmo.to_json()

import urllib2

data = urllib2.urlopen("https://raw.githubusercontent.com/InsightDataScience/coding-challenge/master/data-gen/venmo-trans.txt").read()
data = data.split("\n") # then split it into lines
f = data

open('Venmo.txt', 'r')

data = []
with open('/Users/Chak/Documents/GitHub/Coding-Challenge/Venmo_input/Venmo.txt') as f:
    for line in f:
        data.append(json.loads(line))