import matplotlib.pyplot as plt

#basic plot
x=[1,2,3,4,5]
y=[10,11,12,13,14]
# plt.plot(x,y,color="blue",marker='^',linestyle='--',linewidth=2)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("My First Graph")
# plt.grid(True)
x1=[1,4,9,16,25]
y1=[100,121,144,16,196]
# plt.plot(x,x1,label="X-X1 GRAPH")
# plt.plot(x,y1,label="X-Y1 GRAPH")
# plt.legend()

#bar graph
categories = ['A','B','C','D']
values = [10,18,29,56]

# plt.barh(categories,values,color = 'blue')
# plt.title("Bar Chart ")
a =[5,7,6,3,12,11]
b =[89,67,56,45,81,90]
# plt.scatter(a,b,color='blue')
# plt.title("SCATTER GRAPH")

# histogram
import numpy as np
data = np.random.randn(1000)
# plt.hist(data,bins=30,color='teal',edgecolor='black')
# plt.title("Histogram of Random Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")

sizes = [30,40,15,15]
labels = ['python','Java','c++','JavaScript']

# plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
# plt.title("programming language usage")
# plt.axis('equal')

x=[1,2,3,4,5]
y=[5,7,8,9,8]
plt.subplot(1,2,1)
plt.plot(x, y)
plt.subplot(1,2,2)
plt.bar(x, y)
plt.tight_layout()
plt.savefig("plot.png",dpi=300)
plt.show()



