# 5x5 matrix extract the middle 3x3 
import numpy as np

arr =  np.arange(1,26).reshape(5,5)
print(arr)
print(arr[1:4,1:4])
# here we are slicing the matrix
# 1to 4 mean 1to3 because it takes till n-1 and we r 
# gettting this as (row1,row2,row3) etc etc