from client import DiffbotClient,DiffbotCrawl
from config import API_TOKEN
import csv
import pandas as pd
import pprint
import time
import json
from itertools import islice

df = pd.read_csv("Interactive Media Bias Chart - Ad Fontes Media.csv")

contents = []
with open("Interactive Media Bias Chart - Ad Fontes Media.csv",'r') as csvf: # Open file in read mode
    urls = islice(csv.reader(csvf), 1902, None)
    for url in urls:
        contents.append(url) # Add each url to list contents

my_dict = {}
count = 0
json_count = 39
def diffbotScrape(my_url):
    global count
    global json_count
    global my_dict
    count = count + 1
    diffbot = DiffbotClient()
    token = "2587daf076cad7bba4e58fd272780b2d"
    url = my_url
    api = "article"
    response = diffbot.request(url, token, api, fields=['title', 'type'])
    print ("\nPrinting response:\n")
    print (count)
#forgot to add to my dict before adding it to tthe json

    my_dict[my_url] = response
    print ("Writing to my_dict...\n")
    if (count == 15):
        file = "diffbot" + str(json_count) + ".json"
        with open(file,  'a+') as f:
             json.dump(my_dict, f, sort_keys = True, indent = 4)
        count = 0
        json_count += 1
        my_dict = {}
    #Writing JSON data
# for url in contents:
#     print(url[1])
#     print(url)
for url in contents:
      diffbotScrape(url[1])
      print(url)

# print ("Writing to json...\n")
# with open(r'tester.json', 'a+') as f:
#      json.dump(my_dict, f, sort_keys = True, indent = 4)
