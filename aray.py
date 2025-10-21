import numpy as np

# 1D array
arr1 = np.array([1,2,3,4])
print(arr1)
print(arr1.shape)

# 2d array
arr2 = np.array([[1,2,3,4],
                [5,6,7,8]])
print(arr2)
print(arr2.shape)
# 
# operations on arrays

zer = np.zeros((3,4))
# to create a zero matrix/array
print(zer)

on = np.ones((3,4))
# to create unit matrix/array of omnly 1
print(on)

# here we can get the data type we want with ponts and more
d3 = np.zeros((2,3),dtype=float)
print(d3)

# create a matrix of ur choice 
# syntax ARANGE(start,end,steps)
new_array = np.arange(1,50,5)
# 1 to 50 is raange with an interval of 5 units
print(new_array)

# lin space is used to give equally spaced numbers nummber of entity user asks
# synatax LINSPACE(start,stop,entity = " ",endpoitn)
lin = np.linspace(1,30,10)
print(lin)

# array can under go scalar addition and scalar multiplication

# indexing and slicing

arr5 = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [56,67,78,90]])

print("first row-=",arr5[0])#array in tht row
print("element at (1,2)",arr5[1,2])#taking one element at a time
print("first two rows",arr5[0:2])

