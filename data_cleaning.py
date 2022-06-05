
##_____________________Data_Cleaning________________________________##

import pandas as pd 
import numpy as np 

a=pd.read_csv("ex.csv")
#print(a)

print(a.notnull)
print(pd.notnull(a).count())
print(pd.isnull(a).count())


s = pd.Series(['a', 3, np.nan, 1, np.nan])

print(s.notnull().sum())
print(s.isnull().sum())