import sys
import string
import os 
import csv


name="Sonar_all_data.csv"

data=open(name, "r")
reader= csv.reader(data)
#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in reader:
    xList.append(line)


print ("Number of Rows of Data = ", len(xList))
print ("Number of Columns of Data = ", len(xList[1]))
