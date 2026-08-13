class Solution:
    def matrixReshape(self, mat, r, c):
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        res = []
        flat_list = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res.append(mat[i][j])

        for i in range(r):
            row = []
            for j in range(c):
                row.append(res[i * c + j])
            flat_list.append(row)
        return flat_list


mat = [[1, 2], [3, 4]]
mesin_hitung = Solution()
print(mesin_hitung.matrixReshape(mat, 1, 4))
