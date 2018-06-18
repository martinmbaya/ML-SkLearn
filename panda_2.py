import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import os
import csv

os. chdir('C:\Users\Martin Mbaya\Desktop\Parseltongue\ML')
name="Sonar_all_data.csv"

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(name,header=None, prefix="V")

#assign color based on "M" or "R" labels
for i in range(208):
	if rocksVMines.iat[i,60] == "M\n":
		pcolor = "red"
	else:
		pcolor = "blue"
		
	#plot rows of data as if they were series data
	dataRow = rocksVMines.iloc[i,0:60]
	dataRow.plot(color=pcolor)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()