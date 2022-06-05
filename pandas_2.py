import pandas as pd 
import numpy as np

# working conditional and boolean in series

lst1=pd.Series([26,44,56,78,90,13,34,100])
print(lst1)

# performing operations 

lst2=lst1+1
print("_______added 1 to all members_______")
print(lst2)

lst3=lst1 > 20
print("_______values which are lessthan 20_______")
print(lst3)

lst4=(lst1.mean())
print("_______mean of series________")
print(lst4)

lst5=(lst1.std())
print("_______standardviation of series_________")
print(lst5)


lst6=(lst1.var())
print("_________variance of series ______________")
print(lst6)
