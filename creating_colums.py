import pandas as pd 
import numpy as np


data=pd.read_csv("ex.csv")
#print(data)

# creating colums and preforming operation
data["new_col"]=(data["s_no"]/data["marsk"])
#print(new_col)

print(data)

print(data.describe())




