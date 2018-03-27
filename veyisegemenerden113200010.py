
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from collections import Counter


# In[2]:


dataFrame = pd.read_csv(
    '/Users/veyisegemenerden/Desktop/cmpe407/data.csv')

X=dataFrame.iloc[:,:-1] 
Y=dataFrame.iloc[:,3]


# In[3]:


def splitData(df,r): 
    count = len(df)*r

    return  df[:int(count)], df[int(count):] 



# In[4]:


def euclidDist(train, test):
    return np.sqrt((np.square(train[:,np.newaxis]-test).sum(axis=2)))



# In[5]:


def predict(dist,k,Ytrain):
    vote_result=[]
    for i in range(len(X_test)):
        vote=[]
        result = sorted(range(len(dist[i])), key=lambda k: dist[i][k])
        
        for j in range(k):
            vote.append(Ytrain[result[j]])
        c = Counter(vote)    
        vote_result.append(c.most_common(1))
    return vote_result
    


# In[6]:


def compare(Y_test,pred):
    result=[]
    countOfFalse = 0
    countOfTrue = 0
    for i in range(len(pred)):
        if (pred[i][0][0]==Y_test[i+len(Y_train)]):
            result.append("true")
            countOfTrue += 1
        else:
            result.append("false")
            countOfFalse += 1
        
    return result,countOfTrue,countOfFalse



# In[7]:


def accuracy(countOfTrue,y_test):
    return countOfTrue/len(y_test) * 100


# In[8]:


X_train ,X_test =splitData(X,0.8)


# In[9]:


Y_train ,Y_test =splitData(Y,0.8)


# In[10]:


A = euclidDist(X_test.values, X_train.values)


# In[11]:


of= predict(A,1,Y_train)
result,countOfTrue,countOfFalse=compare(Y_test,of)
acc = accuracy(countOfTrue,Y_test)
print(result)
print('/n')
print("accuracy ", acc)
print('/n')
print("countOfTrue = ",countOfTrue)
print("countOfFalse =", countOfFalse)


# In[12]:


of= predict(A,3,Y_train)
result,countOfTrue,countOfFalse=compare(Y_test,of)
acc = accuracy(countOfTrue,Y_test)
print(result)
print('/n')
print("accuracy ",acc)
print('/n')
print("countOfTrue = ",countOfTrue)
print("countOfFalse =", countOfFalse)

