import numpy as np
try:
    num = int(input ("How many numbers You want to generate :"))

    arr = np.random.randint(10,100,num)
    print("Generated 1D array :",arr)

    print("\nMean :", np.mean(arr))
    print("Median :", np.median(arr))
    print("Standard Deviation :", np.std(arr))
    print("Minimum Value :", min(arr))
    print("Minimum Value:", max(arr))


            # Reshape into a 2D array (if possible)
    if num % 2 == 0:
        matrix = arr.reshape(num // 2, 2)

        print("\n2D Array:")
        print(matrix)

        print("\nRow-wise Sum:")
        for i in matrix:
            print(sum(i))
    else:
        print("\nCannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Invalid input! Please enter an integer.")
except Exception as e:
    print("Error:", e)


