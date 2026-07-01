import numpy as np

arr = np.random.randint(1,50,20)
print(arr)

reshaped_arr = arr.reshape(4,5)
print("\n Reshaped Array (4 x 5)")
print(reshaped_arr)

print("\n Sum of Matrix :", sum(reshaped_arr))

print("\n Mean of Matrix :", np.mean(reshaped_arr))

print("\n Standard deviation of Matrix :", np.std(reshaped_arr))

# Maximum value in each row
print("Maximum value in each row:")

for i in reshaped_arr :
    print(max(i))


