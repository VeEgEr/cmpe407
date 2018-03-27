# Project Title

According to given features predicting student will pass or fail.

## Getting Started

This project was written with python. python3 command helps you for deployment.
Exp:

python3 veyisegemenerden113200010.py   

Also you can download jupyter notebook for deployment.
pip3 install jupyter notebook
jupyter notebook
and than select  veyisegemenerden113200010.py   

### Prerequisites

python3.6 was used in this project.

This project requires to import library of numpy,pandas and collections.

### Installing
Firstly, import library to project.
```
import numpy as np
import pandas as pd
from collections import Counter
```
Secondly,to read cv file and set your dataframe.

```
dataFrame = pd.read_csv(
    'your_filePath')

X=dataFrame.iloc[:,:-1] 
Y=dataFrame.iloc[:,3]
```

Thirdly, define all function.
```
def splitData(df,r): 
def euclidDist(train, test):
def predict(dist,k,Ytrain):
def compare(Y_test,pred):
```
Lastly, run all function sequential.
```
X_train ,X_test =splitData(X,0.8)
Y_train ,Y_test =splitData(Y,0.8)
A = euclidDist(X_test.values, X_train.values)
of= predict(A,1,Y_train)
result,countOfTrue,countOfFalse=compare(Y_test,of)
acc = accuracy(countOfTrue,Y_test)
```
OUTPUT:
['true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true']
/n
accuracy  100.0
/n
countOfTrue =  20
countOfFalse = 0


## Versioning

 for version information. to Check the [cmpe407 on this repository](https://github.com/your/project/tags). 

## Authors

* **Veyis Egemen ERDEN** -[VeEgEr](https://github.com/VeEgEr)




## Acknowledgments

* Euclidean
* Knn
* etc
