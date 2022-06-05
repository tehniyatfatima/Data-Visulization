##_______Mean_Variance_standardiation_calculator__________##

#import pandas module
import pandas as pd     


# take input liat from user
lst=[]
n=int(input("enter lenght of series : "))
for i in range(n):
    member=int(input("enter series numbers : "))
    lst.append(member)


# calculations#
series=pd.Series(lst)

m=(series.mean())
print(m)

v=(series.var())
print(v)

s=(series.std())
print(s)

##_________Final Output__________##

print("____________ Your Result _____________")
print("Given series :"  ,lst)
print("_____________ Lenght of our series___________")
print(len(series))

print("Mean :",m)
print("variance :",v)
print("standardviation :",s)

print("_________Thnaks for using this calculater___________")
input("please press enter for close program") 




