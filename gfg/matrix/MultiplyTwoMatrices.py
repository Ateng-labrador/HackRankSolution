class Solution:
    def multiplyMatrices(self, a, b):
        res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                for k in range(len(b)):
                    res[i][j] += a[i][k] * b[k][j]
        return res

a = [[7, 8], [2, 9]]
b = [[14, 5], [5, 18]]
a1 = [[17, 4], [17, 16]]
b2 = [[9, 2], [7, 1]]
mesin_hitung = Solution()
print(mesin_hitung.multiplyMatrices(a, b))
print(mesin_hitung.multiplyMatrices(a1, b2))
