import pandas as pd 
import numpy as np

data=pd.read_csv("ex.csv")

print(data)

print(data.duplicated())
print(data.duplicated().sum())