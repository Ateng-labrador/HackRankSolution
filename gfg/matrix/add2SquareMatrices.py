class Solution:
    def addMat(self, a, b):
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] += b[i][j]
        return a

    def addMat1(self, a, b):
        res = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                res[i][j] = a[i][j] + b[i][j]
        return res

    def MultyMat(self, a, b):
        res = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                for k in range(len(b)):
                    res[i][j] += a[i][k] * b[k][j]
        return res


a = [[1, 2], [3, 4]]
b = [[3, 4], [2, 1]]
mesin_hitung = Solution()
print(mesin_hitung.addMat(a, b))
