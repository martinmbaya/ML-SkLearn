import csv
import os
import csv

os. chdir('C:\Users\Martin Mbaya\Desktop\Parseltongue\ML')
name="Sonar_all_data.csv"

data=open(name, "r")
reader= csv.reader(data)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in reader:
    xList.append(line)

nrow = len(xList)
ncol = len(xList[1])
type = [0]*3
colCounts = []

#generate summary statistics for column 3 (e.g.)
col = 60
colData = []
for row in xList:
	colData.append(row[col])

for i in range(len(colData)):
	cell=colData[i]
	colData[i]=cell[0]


with open(name, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
        	rowe = string.split(line, ",")
        	writer.writerow(rowe)



