"""
leetcode 2022. Convert 1D Array Into 2D Array

Dalam mengerjakan Soal ini bayangkan anda mempunyai sebuah
balok kayu panjang x, balok ini di potong menjadi m(row(baris)) bagian
karna n(column) in harus mempunyai interval yang sama (column(i % n))
"""

class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(original)):
            row = i // n
            colmn  = i % n
            res[row][colmn] = original[i]
        return res


x = [1,2,3]
mesin_hitung = Solution()
print(mesin_hitung.construct2DArray(x, 1, 3))

        