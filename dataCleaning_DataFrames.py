##____________WorkingWith DataCleaning In Data Frame _______________________##

import pandas as pd 
import numpy as np

x=pd.read_csv("ex.csv")
print(x.isnull())          # used to find null value in data Frame
print(x.isnull().sum())    # to find total no of null value 

print(x.info())
print(x.describe())
print(x.size)
print(x.shape)

print(x.dropna())       # drop na method is used to skip that line , in which any 
                        # value is present


s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')

print(s)

##____________Filling null data___________________##








