from app.creastimate import creastimate_main as cm
from app.creastimate.models import User
from app import create_app, db
from sqlalchemy import exc,asc, desc, and_, or_
import datetime

from flask import session as login_session, json, jsonify
import requests
# from app.auth import authentication as at
from flask_login import login_required
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, redirect, url_for, flash # for flash messaging

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from itertools import combinations
from sklearn.metrics import f1_score
import csv
# from app import socketio

# from flask_socketio import SocketIO, emit, join_room, leave_room, \
#     close_room, rooms, disconnect


@cm.route('/')
def demographics():
    return render_template("index.html")

@cm.route('/input')
def input():
    return render_template("one.html")

@cm.route('/output')
def output():
    return render_template("two.html")

@cm.route('/create')
def create():
    return render_template("three.html")

@cm.route('/SVM', methods=['GET', 'POST'])
def SVM():

    if request.method == 'POST':
        data = request.get_json()

        numOfUniqueWords = float(data['numOfUniqueWords'])
        numOfDifficultWords = float(data['numOfDifficultWords'])
        smartHomeXP = float(data['smartHomeXP'])
        familySize = float(data['familySize'])



        print('numOfDifficultWords', type(numOfDifficultWords))
        print('numOfUniqueWords', type(numOfUniqueWords))
        print('smartHomeXP', type(smartHomeXP))
        print('familySize', type(familySize))

        # print(type(numOfUniqueWords))
        #
        # #----------------------------------------------------------------------------------
        pathtoCsv = 'https://raw.githubusercontent.com/tahir80/Flask-Book-Catalog/master/scenarios.csv'
        ds = pd.read_csv(pathtoCsv, error_bad_lines=False)

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

        X =[[float(numOfUniqueWords), float(numOfDifficultWords), float(smartHomeXP), float(familySize)]]
        y =cls.predict(X)

        print(type(y))

        result = y[0]
        result = str(result)

        return jsonify(result)
