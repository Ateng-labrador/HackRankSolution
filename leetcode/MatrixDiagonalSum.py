class Solution1:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][len(mat) - 1 - 1]
            for j in range(len(mat[0])):
                if i == j:
                    res += mat[i][j]
        if len(mat) % 2 != 0:
            total -= mat[len(mat) // 2][len(mat) // 2]

        return res

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][len(mat) - 1 - i]
        if len(mat) % 2 != 0:
            total -= mat[len(mat) // 2][len(mat) // 2]
        return total

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mesin_hitung = Solution1()
print(mesin_hitung.diagonalSum(x))
