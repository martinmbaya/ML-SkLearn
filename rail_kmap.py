from sklearn import datasets 
import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt

iris = pd.read_csv("To_Train.csv", delimiter ="\t")

# let's remove spaces from column name 
# iris.columns = iris.columns.str.replace(' ','')
iris.head()

X = iris.ix[:, :6]
# [['Distance1', ' Distance2', ' Temperature', ' X_Axis', ' Y_Axis', ' Z_Axis', ' Vibration_state']] # independent variables \
y = iris.Condition   # dependent variable 
sc = StandardScaler() 
sc.fit(X) 
X = sc.transform(X)

# K Means Cluster 
model = KMeans(n_clusters=2, random_state=11) 
model.fit(X) 
print((model.labels_))

# since its unsupervised the labels have been assigned 
# not in line with the actual lables so let's convert all the 1s to 0s and 0s to 1s 

iris['pred_Condition'] =  np.choose(model.labels_, [1,0]).astype(np.int64)
print("Accuracy :", metrics.accuracy_score(iris.Condition, iris.pred_Condition)) 
print("Classification report :", metrics.classification_report(iris.Condition, iris.pred_Condition))

# Set the size of the plot 
plt.figure(figsize=(10,7))

# Create a colormap 
colormap = np.array(['red', 'blue'])
Condition = [int(i) for i in iris.Condition]
print(Condition)


# Plot Deflection distance
plt.subplot(1,2,1)
plt.scatter(iris['Distance1'], iris[' Distance2'], c=colormap[Condition], marker='o', s=50)
plt.xlabel('Distance1 (cm)') 
plt.ylabel('Distance2 (cm)') 
plt.title('Distance (Actual)')

plt.subplot(1,2,2)
plt.scatter(iris['Distance1'], iris[' Distance2'], c=colormap[iris.pred_Condition], marker='o', s=50)
plt.xlabel('Distance1 (cm)') 
plt.ylabel('Distance2 (cm)') 
plt.title('Distance (Actual)')
plt.show()