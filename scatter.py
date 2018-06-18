import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
import os 

os. chdir('C:\Users\Martin Mbaya\Desktop\Parseltongue\ML')
name="Sonar_all_data.csv"


#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(name,header=None, prefix="V")
#calculate correlations between real-valued attributes

dataRow2 = rocksVMines.iloc[1,0:60]
dataRow3 = rocksVMines.iloc[2,0:60]

plot.scatter(dataRow2, dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()

dataRow21 = rocksVMines.iloc[20,0:60]
plot.scatter(dataRow2, dataRow21)

plot.xlabel("2nd Attribute")
plot.ylabel(("21st Attribute"))
plot.show()