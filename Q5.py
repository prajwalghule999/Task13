import numpy as np

arr1 = np.random.rand(10) 
print("A 1D array of 10 random numbers between 0 and 1 :")
print(arr1)

arr2 = np.random.randn(9).reshape(3,3)
print("A 3x3 matrix of random numbers :")
print(arr2)

arr3 = np.random.randint(10,51,(4,5))
print("4x5 Random Integer Array :")
print(arr3)