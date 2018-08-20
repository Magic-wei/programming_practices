#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# step 1: Importing the libraries

import numpy as np
import pandas as pd

# step 2: Importing dataset
## I have to learn basic knowledge of pandas

dataset = pd.read_csv('Data.csv')
print(dataset)
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values
print(X)
print(Y)

# Step 3: Handling the missing data
## I have to learn basic knowledge of sklearn.processing
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
print('X after handling the missing data:\n',X)

# Step 4: Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
print('X after encoding categorical data:\n',X)

## Creating a dummy variable

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
print('Y after encoding categorical data:\n',Y)

# Step 5: Splitting the datasets into training sets and Test sets

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
print('training partition and test partition:\n')
print('X_train:\n',X_train)
print('Y_train:\n',Y_train)
print('X_test:\n',X_test)
print('Y_test:\n',Y_test)

# Step 6: Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
print('X_train after Feature Scaling:\n',X_train)
print('X_test after Feature Scaling:\n',X_test)

# Done!
