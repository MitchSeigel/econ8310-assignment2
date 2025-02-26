# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RosvuK9jo_5V8xTXWOMK4IS2DDzWSpt2
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train_data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3.csv")

test_data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3test.csv")

X_train = train_data.drop(columns=['id','DateTime','meal'])
y_train = train_data['meal']

X_test = test_data.drop(columns=['id','DateTime','meal'])

# model = RandomForestClassifier(n_estimators=200, max_depth=50)
model = DecisionTreeClassifier(max_depth=100, min_samples_leaf=10)

modelFit = model.fit(X_train, y_train)

pred = modelFit.predict(X_test)

pred = pred.astype(int)
pred = pred.tolist()
pred