class Solution:
    def rowSum(self, mat):
        res = []
        for i in range(len(mat)):
            Sres = 0
            for j in range(len(mat[0])):
                Sres += mat[i][j]
            res.append(Sres)
        return res
            

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[1, 2], [10, 2], [3, 3]]
mesin_hitung = Solution()
print(mesin_hitung.rowSum(x))
print(mesin_hitung.rowSum(y))
