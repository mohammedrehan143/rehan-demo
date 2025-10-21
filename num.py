import numpy as np
import time

# we r using this to get the time taken by python list
# and numpy array
# python list
list_data = list(range(1_000_000))
start1 = time.time()
sum_list = sum(list_data)
end1 = time.time()
print("python list time:", end1 - start1)

# numpy array
array_data = np.array(1_000_000)
start2 = time.time()
sum_array = np.sum(array_data)
end2 = time.time()
print("numpy array time :",end2 - start2)