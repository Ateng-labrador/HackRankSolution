import numpy as np

def makearray(arr):
    return np.flip(np.array(arr, float))

arr = input().strip().split(' ')
print(makearray(arr))

