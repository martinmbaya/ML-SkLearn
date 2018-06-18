import numpy as np
import sys
import os
import csv
import scipy.stats as stats
import pylab


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
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()