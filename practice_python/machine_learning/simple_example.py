#! /usr/bin/env python3
# -*- coding = utf-8 -*-

import numpy as np
import sklearn.linear_model as skl
import pylab as py
import pandas as pd
import seaborn as sb

model = skl.LinearRegression()

xval = np.array([1,2,3,4,5]).reshape(-1,1)
yval = [1,2,3,4,7]

model.fit(xval, yval)

print(model.predict(12))
print(model.predict(1))

py.figure()
py.scatter(xval,yval)
py.show()

