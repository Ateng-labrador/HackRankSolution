class Solution:
    def sumOfMatrix(self, mat):
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res += mat[i][j]
        return res

x = [[1, 0, 1], [-8, 9, -2]]
mesin_hitung = Solution()
print(mesin_hitung.sumOfMatrix(x))

