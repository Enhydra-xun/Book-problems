#/  import csv

import csv
csvFile = open("SpeedVideoDataforModeling.csv", "r")
reader = csv.reader(csvFile)
listcount=[]
for item in reader:
    listcount.append(item[0])

count=len(listcount)
print count
