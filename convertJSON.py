import csv
import json
from itertools import islice
import pandas as pd

contents = []
with open("Interactive Media Bias Chart - Ad Fontes Media.csv",'r') as csvf: # Open file in read mode
    urls = islice(csv.reader(csvf), 1, None)
    for url in urls:
        contents.append(url) # Add each url to list contents
f = csv.writer(open("diffbotData.csv", "w", encoding="utf-8"))
f.writerow(['Title', 'Author', 'Date', 'EstimatedDate', 'Text'])
# json_file = open('diffbot2.json',  encoding="utf-8")
# read_json = json_file.read()
# data = json.loads(read_json)


def convert_to_csv(my_url, data):
    if my_url in data:

        main_bigR = data[my_url]
        if 'objects' in main_bigR:
            main_big = data[my_url]['objects'][0]
            tagCount = 0
            date = "N/A"
            author = "N/A"
            title = "N/A"
            text = "N/A"
            estimatedDate = "N/A"
            for info in main_big:
                if 'date' in info:
                    date = main_big['date']
                if 'author' in info:
                    author = main_big['author']
                if 'text' in info:
                    text = main_big['text']
                if 'title' in info:
                    title = main_big['title']
                if 'estimatedDate' in info:
                    title = main_big['estimatedDate']

                    # Write CSV Header, If you dont need that, remove this line
            f.writerow([title,
                        author,
                        date,
                        estimatedDate,
                        text])

number_of_file = 0
for jsoncount in range(1, 39):
    for url in contents:
        file = "diffbot" + str(jsoncount) + ".json"
        df = pd.read_json(file)
        df.to_csv('test.csv', mode = 'a')
        number_of_file += 1
        print(number_of_file)

        # df = pd.read_json(file)
        # df = df.items(file)
        # stringUrl = (url[1])
        # df = df.loc[[[["count", "label", "rdfTypes", "score"], "tags",  "author", "authorUrl", "date", "estimatedDate", "siteName", "text", "title"], "objects"],str(stringUrl)].T
        # df = df.append(pd.Series(df["tags"]["count"], df["tags"]["label"], df["tags"]["rdfTypes"], df["tags"]["score"],\
        #                         df["objects"]["tags"], df["objects"]["author"], df["objects"]["authorUrl"],\
        #                         df["objects"]["date"], df["objects"]["estimatedDate"], df["objects"]["siteName"], df["objects"]["text"],\
        #                         df["objects"]["title"], df[str(stringUrl)]["objects"]))
        # df.to_csv("diffbotDataTest.csv")
        # json_file = open(file,  encoding="utf-8")
        # read_json = json_file.read()
        # data = json.loads(read_json)
        # convert_to_csv(url[1], data)
print("Finished converting")
