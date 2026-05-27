import numpy as np

# my_array = np.array([i for i in range(6)])
# #(6,) -> 1 row and 6 columns
# my_array_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# my_array.shape = (2, 3)
# print(np.reshape(my_array, (3, 2)))

# shape memberikan tuple dari dimensi arrray dan dapat digunakan untuk mengubah
# dimensi dari array

# reshape tool untuk membuat shape baru ke dalam array tanpa mengubaha data asli\
# membuat data baru tanpa mengubah data itu sendiri

def makearr(arr):
    arr_new = np.array([arr], int)
    return np.reshape(arr_new, (3, 3))


arr = input().strip().split()
print(makearr(arr))
