import numpy as np
# a = np.array([1,2,3])
# b = np.array([45])
# c = np.array([[1,2],[3,9]])
# d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# #check the dimension of the array 
# print(a.ndim)
# print(a)
# #ndmin 
# arr = np.array([1,2,3,4],ndmin=5)
# print(arr.ndim)
# print(arr.dtype)
# print(c.ndim)
# print(c[1,0])
# print(d[0,2,2])
# #print(d[1,0,0])
# print(a[0:4:2])#slicing one 1d array
# c1= np.array([[1,2,5,6,7],[3,4,8,9,10]])
# print(c1[1,1:4])#slice ele from 1 to 4 in the index 1 of the array
# print(c1[0:2,2])#slice index 2 from both the ele in arr
# print(c1[0:2,1:4])#slice ele from 1 to 4 index in the arr
# print(c1.shape)

#common creaters in numpy 
print(np.zeros((2,3)))#2*3 array of zeros
print(np.ones((3,)))#id array of 3 elements
print(np.eye(3))#identity matrix
print(np.arange(1,10,2))#same as like for loop
print(np.linspace(0,1,5))

d1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d2 = d1.reshape(2,6)
print(d2)

arr2 = np.array([[1,2,3,4],[4,5,6,9]])
d3 = arr2.reshape(8,)
print(d3)
#flatten method is used to convert  a 2d arr to 1d arrr
print(arr2.flatten())

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y)
print(x*2)
print(np.sqrt(x))
y1 = np.array([[1],[2],[3]])
print(x+y1)

z = np.array([[1,2],[3,4]])
print(z.sum())
print(z.max(axis=0))#finds max value in each column
print(z.mean())
print(np.median(z))

#boolean indexing and masking

z1 = np.array([1,2,3,4,5,6,7,8,9,10])
mask = z1%2==0
print(z1[mask])

mark = np.array([25,40,50,60,70])
marks = mark+5
mask = marks<=35
print(marks[mask])
