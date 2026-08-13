class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [max(matrix[r][c] for r in range(m)) for c in range(n)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = res[j]
        return matrix

mesin_hitung = Solution()
x = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
print(mesin_hitung.modifiedMatrix(x))
                