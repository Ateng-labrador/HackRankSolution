class Solution1:
    def summat(self, mat):
        res1 = []
        for i in range(len(mat)):
            res = 0
            for j in range(len(mat[0])):
                res += mat[i][j]
            res1.append(res)
        return res1

    def sumOfRowCol(self, mat):
        resf = self.summat(mat)
        for i in range(len(mat)-1):
            if resf[i] != resf[i + 1]:
                return False
        return True
                

class Solution:
    def sumOfRowCol(self, mat):
        for i in range(min(len(mat), len(mat[0]))):

            row_sum = sum(mat[i])
            col_sum = sum(mat[r][i] for r in range(len(mat)))
            if row_sum != col_sum:
                return False
        return True

x = [[1, 2], [2, 1]]
y = [[5], [0], [0]]
z = [[1, 4, 2], [6, 1, 3]]
mesin_hitung = Solution()
print(mesin_hitung.sumOfRowCol(x))
print(mesin_hitung.sumOfRowCol(y))
print(mesin_hitung.sumOfRowCol(z))
