class Solution1:
    def isToeplitz(self, mat):
        def is_diagonal_univalue(row, col):
            val = mat[row][col]
            while row < len(mat) and col < len(mat[0]):
                if mat[row][col] != val:
                    return False
                row += 1
                col += 1
            return True

        for col in range(len(mat[0])):
            if not is_diagonal_univalue(0, col):
                return False

        for row in range(1, len(mat)):
            if not is_diagonal_univalue(row, 0):
                return False

        return True

class Solution2:
    def is_diagonal_univalue(self, mat ,row, col):
        val = mat[row][col]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i+1][j+1] != val:
                    return False
                row += 1
                col += 1
        return True

    def isToeplitz(self, mat):
        for col in range(len(mat[0])):
            if not self.is_diagonal_univalue(mat ,0, col):
                return False
        for row in range(1, len(mat)):
            if not self.is_diagonal_univalue(mat, row, 0):
                return False
        return True


class Solution:
    def isToeplitz(self, mat):
        for i in range(len(mat) - 1):
            for j in range(len(mat[0]) - 1):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False
        return True


x = [[6, 7, 8], [4, 6, 7], [1, 4, 6]]
y = [[6, 3, 8], [4, 9, 7], [1, 4, 6]]
mesin_hitung = Solution()
print(mesin_hitung.isToeplitz(x))
print(mesin_hitung.isToeplitz(y))
