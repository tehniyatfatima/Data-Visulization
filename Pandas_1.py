import pandas as pd 
import numpy as np



# creating series (method no1 )

lst1=(["tehniyat","fatima","shakir fareed","adeena","dua"])
lst2=pd.Series(lst1)
print(lst2)

# creating series (method no 2)
x=pd.Series(["tehniyat","fatima","shakir fareed","adeena","dua"])
print(x)

# indexing 
y=pd.Series(["tehniyat","fatima","shakir fareed","adeena","dua"],index=[1,2,3,4,5])
print(y)

# acess elements by indexing
print(y[1])
print(x[0])
print(x.iloc[1:3])
print(x[1:3]) 




