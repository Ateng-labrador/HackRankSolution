class Solution:
    def diagonalSum(self, mat):
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][len(mat) - 1 - i]
        return res

x = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
y = [[1, 2], [3, 4]]
mesin_hitung = Solution()
print(mesin_hitung.diagonalSum(x))
print(mesin_hitung.diagonalSum(y))

        