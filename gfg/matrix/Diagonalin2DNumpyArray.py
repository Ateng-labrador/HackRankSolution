import numpy as np

class Solution1:
    def diagonalElements(self, arr):
        res = []
        for i in range(len(arr[0])):
            res.append(arr[i][i])
        return res

class Solution:
    def diagonalElements(self, arr):
        return np.diagonal(arr)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]])
mesin_hitung = Solution()
print(mesin_hitung.diagonalElements(x))
print(mesin_hitung.diagonalElements(y))

