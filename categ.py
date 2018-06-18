import numpy as np
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

#generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)

print "\nMean = \t", colMean, "\t\t"
print "Standard Deviation = \t", colsd, "\n"

#calculate quantile boundaries
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

print "\nBoundaries for 4 Equal Percentiles \n"
print percentBdry, "\n"

#run again with 10 equal intervals
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

print "Boundaries for 10 Equal Percentiles\n"	
print percentBdry, "\n"

#The last column contains categorical variables
col = 60
colData = []
for row in xList:
	cell=row[col]
	cell=cell[0]
	colData.append(cell)

unique = set(colData)
print "Unique Label Values \n"
print unique

#count up the number of elements having each value
catDict = dict(zip(list(unique), range(len(unique))))
catCount = [0]*2
for elt in colData:
	catCount[catDict[elt]] += 1

print "\nCounts for Each Value of Categorical Label \n"
print(list(unique))
print(catCount)