import numpy as np

# transposition -> fungsi untuk melakukan transpose pada array
# Flatten -> fungsi untuk membuat array menjadi flatten 
N, M = map(int ,input().split())


arr = []
for _ in range(N):
    x = input().split()
    arr.append(x)

arr_arr = np.array(arr, int)
arr_arr_flat = arr_arr.flatten()
print(np.transpose(arr_arr))
print(arr_arr_flat)

