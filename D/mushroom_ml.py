import numpy
from sklearn import datasets, linear_model
from math import sqrt
import matplotlib.pyplot as plot
import csv 
from tqdm import tqdm
import datetime
import winsound


startt = datetime.datetime.now()
#read data into iterable
name="mushroom_ml.csv"
data=open(name, "r")
reader= csv.reader(data)
xList = []
labels = []
names = []
firstLine = True

for line in tqdm(data):
	if firstLine:
		names = line.strip().split(",")
		firstLine = False
	else:
		#split on semi-colon
		row = line.strip().split(",")
		#put labels in separate array
		labels.append(float(row[-1]))
		#remove label from row
		row.pop()
		#convert row to floats
		floatRow = [float(num) for num in row]
		xList.append(floatRow)

#Normalize columns in x and labels
nrows = len(xList)
ncols = len(xList[0])
#calculate means and variances
xMeans = []
xSD = []
for i in tqdm(range(ncols)):
	col = [xList[j][i] for j in range(nrows)]
	mean = sum(col)/nrows
	xMeans.append(mean)
	colDiff = [(xList[j][i] - mean) for j in range(nrows)]
	sumSq = sum([colDiff[i] * colDiff[i] for i in range(nrows)])
	stdDev = sqrt(sumSq/nrows)
	xSD.append(stdDev)


#Build cross-validation loop to determine best coefficient values.
#number of cross-validation folds
nxval = 2
#number of steps and step size
nSteps = 10000
stepSize = 0.004
#initialize list for storing errors.
errors = []
for i in range(nSteps):
	b = []
	errors.append(b)

for ixval in tqdm(range(nxval)):
	#Define test and training index sets
	idxTest = [a for a in range(nrows) if a%nxval == ixval*nxval]
	idxTrain = [a for a in range(nrows) if a%nxval != ixval*nxval]
	#Define test and training attribute and label sets
	xTrain = [xList[r] for r in idxTrain]
	xTest = [xList[r] for r in idxTest]
	labelTrain = [labels[r] for r in idxTrain]
	labelTest = [labels[r] for r in idxTest]
	#Train LARS regression on Training Data
	nrowsTrain = len(idxTrain)
	nrowsTest = len(idxTest)
	#initialize a vector of coefficients beta
	beta = [0.0] * ncols
	#initialize matrix of betas at each step
	betaMat = []
	betaMat.append(list(beta))
	for iStep in range(nSteps):
		#calculate residuals
		residuals = [0.0] * nrows
		for j in range(nrowsTrain):
			labelsHat = sum([xTrain[j][k] * beta[k]	for k in range(ncols)])
			residuals[j] = labelTrain[j] - labelsHat
		#calculate correlation between attribute columns
		#from normalized wine and residual
		corr = [0.0] * ncols
		for j in range(ncols):
			corr[j] = sum([xTrain[k][j] * residuals[k] for k in range(nrowsTrain)]) / nrowsTrain
		iStar = 0
		corrStar = corr[0]
		for j in range(1, (ncols)):
			if abs(corrStar) < abs(corr[j]):
				iStar = j; corrStar = corr[j]
		beta[iStar] += stepSize * corrStar / abs(corrStar)
		betaMat.append(list(beta))
		#Use beta just calculated to predict and accumulate out of
		#sample error - not being used in the calc of beta
		for j in range(nrowsTest):
			labelsHat = sum([xTest[j][k] * beta[k] for k in range(ncols)])
			err = labelTest[j] - labelsHat
			errors[iStep].append(err)


cvCurve = []
for errVect in errors:
	mse = sum([x*x for x in errVect])/len(errVect)
	cvCurve.append(mse)

minMse = min(cvCurve)
minPt = [i for i in range(len(cvCurve)) if cvCurve[i] == minMse ][0]
print("Minimum Mean Square Error", minMse)
print("Index of Minimum Mean Square Error", minPt)

xaxis = range(len(cvCurve))
endt = datetime.datetime.now()
print('Time taken : ', (endt-startt))
plot.plot(xaxis, cvCurve)

plot.xlabel("Steps Taken")
plot.ylabel(("Mean Square Error"))
plot.show()