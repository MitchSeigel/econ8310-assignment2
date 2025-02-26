# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RosvuK9jo_5V8xTXWOMK4IS2DDzWSpt2
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the training data
train_data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3.csv")

# Load the test data
test_data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/assignment3test.csv")

# Separate features (x) and target (y)
X_train = train_data.drop(columns=['id','DateTime','meal'])
y_train = train_data['meal']

# Features for prediction (test data)
X_test = test_data.drop(columns=['id','DateTime','meal'])

# Create a RandomForestClassifier instance
model = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust hyperparameters

# Fit the model to the training data
modelFit = model.fit(X_train, y_train)

# Make predictions on the test data
pred = modelFit.predict(X_test)

# Convert predictions to binary values (1 or 0)
pred = pred.astype(int)
pred = pred.tolist()
pred

# test_data = test_data.drop(columns='meal')

# test_data['meal'] = pred
# test_data

# Calculate accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy * 100:.2f}%")