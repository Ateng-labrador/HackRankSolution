import numpy as np

class Solution:
    def transposeMatrix(self, arr):
        return np.transpose(arr)

class Solution1:
    def transposeMatrix(self, arr):
        res = [list(i) for i in zip(*arr)]
        return res

x = [[1, 2], [3, 4], [5, 6]]
y = [[7, 8, 9], [10, 11, 12]]
mesin_hitung = Solution1()
print(mesin_hitung.transposeMatrix(x))
print(mesin_hitung.transposeMatrix(y))


