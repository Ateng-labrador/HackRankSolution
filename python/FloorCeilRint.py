import numpy as np
np.set_printoptions(legacy='1.13')

N = input().split()

arr_N = np.array(N, dtype=float)
print(np.floor(arr_N))
print(np.ceil(arr_N))
print(np.rint(arr_N))
