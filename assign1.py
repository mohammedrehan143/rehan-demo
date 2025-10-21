# 5x5 matrix extract the middle 3x3 
import numpy as np

arr =  np.arange(1,26).reshape(5,5)
print(arr)
print(arr[1:4,1:4])
# here we are slicing the matrix
# 1to 4 mean 1to3 because it takes till n-1 and we r 
# gettting this as (row1,row2,row3) etc etc

# create an array with 10 numbers replace even number with oddnumber

numm = np.array([1,2,3,4,5,6,7,8,9,10])
for i in range(0,9):
    if(numm[i]%2==0):
        continue
    else:
        numm[i]+=1
        
print(numm)        


# brpadcasting 

arr1 = np.array([[1,2,3,4],
                 [10,20,30,40],
                 [23,34,45,56],
                 [12,23,57,80]])

mun = np.array([1,2,3,4])
print("array after broadcasting=",arr1+mun)
print((arr1.shape))
print(arr1.reshape(2,8))