from sklearn import datasets 
import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt
iris = datasets.load_iris()

# Let's convert to dataframe 
iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
	columns= iris['feature_names'] + ['species'])

# let's remove spaces from column name 
iris.columns = iris.columns.str.replace(' ','') 
iris.head()

X = iris.ix[:,:3] # independent variables \
y = iris.species   # dependent variable 
sc = StandardScaler() 
sc.fit(X) 
X = sc.transform(X)

# K Means Cluster 
model = KMeans(n_clusters=3, random_state=11) 
model.fit(X) 
print((model.labels_))

# since its unsupervised the labels have been assigned 
# not in line with the actual lables so let's convert all the 1s to 0s and 0s to 1s # 2's look fine 
iris['pred_species'] =  np.choose(model.labels_, [1, 0, 2]).astype(np.int64)
print("Accuracy :", metrics.accuracy_score(iris.species, iris.pred_species)) 
print("Classification report :", metrics.classification_report(iris.species, iris.pred_species))

# Set the size of the plot 
plt.figure(figsize=(10,7))

# Create a colormap 
colormap = np.array(['red', 'blue', 'green'])
species = [int(i) for i in iris.species]
print(species)
# print(iris.pred_species)

# Plot Sepal 
plt.subplot(2, 2, 1) 
plt.scatter(iris['sepallength(cm)'], iris['sepalwidth(cm)'],
	c=colormap[species], marker='o', s=50) 
plt.xlabel('sepallength(cm)') 
plt.ylabel('sepalwidth(cm)') 
plt.title('Sepal (Actual)')

plt.subplot(2, 2, 2) 
plt.scatter(iris['sepallength(cm)'], iris['sepalwidth(cm)'], c=colormap[iris.pred_species], marker='o', s=50) 
plt.xlabel('sepallength(cm)') 
plt.ylabel('sepalwidth(cm)') 
plt.title('Sepal (Predicted)')

plt.subplot(2, 2, 3) 
plt.scatter(iris['petallength(cm)'], iris['petalwidth(cm)'], c=colormap[species],marker='o', s=50) 
plt.xlabel('petallength(cm)') 
plt.ylabel('petalwidth(cm)') 
plt.title('Petal (Actual)')

plt.subplot(2, 2, 4) 
plt.scatter(iris['petallength(cm)'], iris['petalwidth(cm)'], c=colormap[iris.pred_species],marker='o', s=50) 
plt.xlabel('petallength(cm)') 
plt.ylabel('petalwidth(cm)') 
plt.title('Petal (Predicted)') 
plt.tight_layout()
plt.show()