class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [i for i in zip(*matrix)]

    def transpose1(self, matrix: list[list[int]]) -> list[list[int]]:
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res

    def transpose2(self, matrix: list[list[int]]) -> list[list[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mesin_hitung = Solution()
print(mesin_hitung.transpose2(x))
