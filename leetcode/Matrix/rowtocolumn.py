class Solution:
    def rowtocolumn1(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            res.append(row)
        return res

    def rowtocolumn2(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for j in range(len(matrix[0])):
            column_elements = [matrix[i][j] for i in range(len(matrix[0]))]
            res.append(column_elements)
        return res

matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
mesin_hitung = Solution()
print(mesin_hitung.rowtocolumn(matrix))
