import sys
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
for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0]*3

print "Col#\t Number \t Strings\t Other\t"

iCol = 0
for types in colCounts:
	print iCol, "\t\t", types[0], "\t\t", types[1], "\t\t", types[2]
	iCol += 1

