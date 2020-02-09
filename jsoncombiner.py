
import json, csv
from glob import glob

with open('diffboatDataAll.csv', 'w') as  f:
    for fname in glob("*.json"):
        with open(fname) as j:
            f.write(str(json.load(j)))
            f.write('\n')
