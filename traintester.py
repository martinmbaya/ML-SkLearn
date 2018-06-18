import sys
import string
import csv


name="Sonar_all_data.csv"

data=open(name, "r")
reader= csv.reader(data)
#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
	#split on comma
	row = line.strip().split(",")
	#assign label 1.0 for "M" and 0.0 for "R"
	if(row[-1] == 'R'):
		labels.append(0.0)
	else:
		labels.append(1.0)
	#remove lable from row
	row.pop()
	#convert row to floats
	floatRow = [float(num) for num in row]
	xList.append(floatRow)

#divide attribute matrix and label vector into training(2/3 of data)
#and test sets (1/3 of data)
indices = range(len(xList))
xListTest = [xList[i] for i in indices if i%3 == 0 ]
xListTrain = [xList[i] for i in indices if i%3 != 0 ]
labelsTest = [labels[i] for i in indices if i%3 == 0]
labelsTrain = [labels[i] for i in indices if i%3 != 0]

print(labels)
Name="xListTest.csv"

with open(Name, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in xListTest:
        	writer.writerow([line[n] for n in [o for o in range(len(line))]])


