class Solution1:
    """
    Salah
    """
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


class MatrikSalib:
    """
    Diberikan sebuah matriks, jumlahkan semua matriks
    pada membentuk pola positif
    """
    def SalibSum(self, mat: list[list[int]]) -> int:
        res = 0
        if len(mat) % 2 != 0:
            for i in range(len(mat)):
                res += mat[i][len(mat) // 2]
                res += mat[len(mat) // 2][i]
                res -= mat[len(mat) // 2][len(mat) // 2]
        else:
            mid1, mid2 = (len(mat) // 2) - 1, (len(mat) // 2)
            for i in range(len(mat)):
                res += mat[i][mid1] + mat[mid1][i] + mat[i][mid2] + mat[mid2][i]
            res -= (mat[mid1][mid1] + mat[mid1][mid2] + mat[mid2][mid2] + mat[mid2][mid1])
        return res


x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
mesin_hitung = MatrikSalib()
print(mesin_hitung.SalibSum(x))
