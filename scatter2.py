import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import os
from random import uniform 

os. chdir('C:\Users\Martin Mbaya\Desktop\Parseltongue\ML')
name="Sonar_all_data.csv"


#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(name,header=None, prefix="V")

#change the targets to numeric values
target = []
for i in range(208):
	#assign 0 or 1 target value based on "M" or "R" labels
	if rocksVMines.iat[i,60] == "M":
		target.append(1.0)
	else:
		target.append(0.0)

#plot 35th attribute
dataRow = rocksVMines.iloc[0:208,35]
plot.scatter(dataRow, target)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()
#
#To improve the visualization, this version dithers the points a little
# and makes them somewhat transparent
target = []
for i in range(208):
	if rocksVMines.iat[i,60] == "M":
		target.append(1.0 + uniform(-0.1, 0.1))
	else:
		target.append(0.0 + uniform(-0.1, 0.1))

#plot 35th attribute with semi-opaque points
dataRow = rocksVMines.iloc[0:208,35]
plot.scatter(dataRow, target, alpha=0.5, s=120)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()