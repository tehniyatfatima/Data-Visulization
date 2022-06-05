import pandas as pd 
import numpy as np 


# second method of data Frame creation

df=pd.DataFrame
report=pd.read_csv("ex.csv")
print(report)


report2=df(report)
print(report2)

print(report2.tail(2))
print(report2.head(2))

##  Conditional Selection in data frame

print(df(report2["marsk"]) == 90)



# droping off 

print(report2.drop({0,1}))                    # for skiping elements by index
print(report2.drop(columns=["date","s_no"]))  # for skiping columns


## renaming colums and index
print(report2.rename(
    columns={ "marsk":"marks"

    },

    index={2 :"ii"}


))



certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)