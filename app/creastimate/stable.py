#!/usr/bin/env python
# #IMPORTS ---------------------------------------------------------
#import the necessary library (pandas) to read the csv data
import pandas as pd
#import the necessary library from SKLearn to apply the SVM algorithm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from itertools import combinations 
from sklearn.metrics import f1_score
import sys
#----------------------------------------------------------------------------------

#read the data from the scenarios.csv file (I assume it is in the same directory with your Jupyter notebook)
ds =pd.read_csv("scenarios.csv")

#let's find out the unique values in the "Category" column, we will find out that there are 9 unique categories
#ds.Category.unique()

#CONVERT TO NUMERIC VALUES ---------------------------------------------------------
#e.g. convert Category to a numeric value
ds.Category =ds.Category.map({'Entertainment':1, 'Comfort':2, 'Home Security':3, 'Cooking':4, 'Energy Saving':5, 'Child Care':6, 'Health':7, 'Elderly Care':8, 'Pet Care':9})
ds.HasSmarthomeexperience =ds.HasSmarthomeexperience.map({'Yes':1, 'No':0})
ds.Gender =ds.Gender.map({'Male':1, 'Female':0})
ds['Programming Experience'] =ds['Programming Experience'].map({'Beginner':1, 'No experience':2, 'Intermediate':3, 'Expert':4})
#----------------------------------------------------------------------------------

#Train SVM with the features as attribute to the function:
def predictCreativity(ds, features):
    training_set,validation_set =train_test_split(ds, random_state=1)
    classifier =SVC(kernel = 'rbf', gamma ='scale')
    dependent ='Creative'
    classifier.fit(training_set[features], training_set[dependent])
    #find out how good the model performs. score Returns the mean accuracy on the given test data and labels: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.score
    scr =classifier.score(validation_set[features], validation_set[dependent])
    y =classifier.predict(validation_set[features])
    f1 =f1_score(validation_set[dependent], y)
    return scr, f1, classifier

bestFeatures =['UW', 'DW', 'Total Experience (Months)', 'Family Size']
s, f1, cls =predictCreativity(ds, bestFeatures)

X =[[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]]
y =cls.predict(X)
print(y)