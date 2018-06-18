import urllib3
import sys
import string
import os
import csv

http = urllib3.PoolManager()
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
response = http.request('GET', target_url)


data = response.data
data = data.decode("utf-8")
name="Sonar_all_data2.csv"

with open(name, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
        	line=str(line)
        	rowe=line.split(",")
        	writer.writerow(rowe)

