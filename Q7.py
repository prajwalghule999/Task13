import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

print("Adition of Matrix :")
print(A+B)

print("\n Matrix multiplication")
print(A@B)

print("\n Element-wise multiplication (*)")
print(A*B)