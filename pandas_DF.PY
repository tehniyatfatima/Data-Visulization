import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame 

## working with data frames:

# x=pd.read_csv("ex.csv")
# print(x)



r_no={"20B-114-SE":"Tehniyat Fatima",
      "20B-060-SE":"Adeena Hussain",
      "20B-095-DE":"Dua Ali",
      "20B-034-SE":"Aisha Saeed",
      "20B-084-SE":"Sharoz Ali"}

sec={"20B-114-SE":"A",
      "20B-060-SE":"A",
      "20B-095-DE":"B",
      "20B-034-SE":"C",
      "20B-084-SE":"D"}

dep={"20B-114-SE":"SE",
      "20B-060-SE":"SE",
      "20B-095-DE":"SE",
      "20B-034-SE":"SE",
      "20B-084-SE":"SE"}
sem={"20B-114-SE":"First Semester",
      "20B-060-SE":"First Semester",
      "20B-095-DE":"First Semester",
      "20B-034-SE":"First Semester",
      "20B-084-SE":"First Semester"}

uni={"20B-114-SE":"UIT",
      "20B-060-SE":"UIT",
      "20B-095-DE":"UIT",
      "20B-034-SE":"UIT",
      "20B-084-SE":"UIT"}

stu_data=pd.DataFrame({"NAME OF STUDENT":r_no,"SECTION":sec,"DEPARTMENT":dep,"SEMESTER":sem,"INSTITUTE NAME":uni})
#print(stu_data)



print(stu_data.index)
print(stu_data.columns)

print(stu_data.info())
print(stu_data.shape)          
print(stu_data.size)
print(stu_data.describe())
print(stu_data.dtypes)
print(stu_data.dtypes.value_counts())


## Data Frame Indexing and slicing 

print(stu_data.head(2))              # if we want to  show upper data
print(stu_data.tail(1))              # if we want to show lower data
print(stu_data.loc["20B-114-SE"])    # select by index
print(stu_data.iloc[-1])               # select by sequencial position





