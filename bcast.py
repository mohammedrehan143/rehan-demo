# broadcasting of an array :it alllows to perforn operations bw diff 
# shapes as long as they r compatible eg adding ia array to each row od a 2d array

import numpy as np

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,8,99,89]])

b = np.array([10,20,30,40])

print("broadcasted result",a+b)

# assignment 
#1 Creatw 5x5 matrix of array,extract the middle 3x3 matrix block
# 2 create an array of 10 numbers replace all even numbers with odd numbers
# 3 try broad casting add[1,2,3,4] to 4x4 array
