##__________________________Ploting_Simple_Graphs________________________________##

from matplotlib import pyplot as plt

x=[2,4,6,8,10]
y=[1,3,5,7,9]
x1=[5,8,10,11,12]
y2=[0,1,9,2,11]
plt.plot(x,y)
plt.plot(x1,y2)
plt.title("sample graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(["first line","second line"])
plt.show()


