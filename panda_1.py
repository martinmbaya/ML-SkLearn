import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import os

#target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")


os. chdir('C:\Users\Martin Mbaya\Desktop\Parseltongue\ML')
name="Sonar_all_data.csv"

#data=open(name, "r")
#reader= csv.reader(data)

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(name,header=None, prefix="V")

#print head and tail of data frame
print(rocksVMines.head())
print(rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()
print(summary)