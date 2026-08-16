class Solution:
    def countZeros(self, mat):
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    res += 1
        return res

x = [[0,0,0], [0,0,1], [0,1,1]]
y = [[1,1], [1,1]]
mesin_hitung = Solution()
print(mesin_hitung.countZeros(x))
print(mesin_hitung.countZeros(y))
