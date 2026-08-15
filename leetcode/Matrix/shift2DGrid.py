"""
1260
"""

# aturan 1: Elemen biasa geser 1 langkah ke kanan
#  Aturan 2: elemen ujung kanan baris pindah ke awal baris berikutnya
# Aturan 3: Elemen ujung kanan bawah [m - 1][n - 1] pindah ke [0][0]

class Solution:
    def shiftMatrix(self, grid):
        res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j < len(grid[0]) - 1:
                    res[i][j + 1] = grid[i][j]
                elif i < len(grid) - 1:
                    res[i + 1][0] = grid[i][j]
                else:
                    res[0][0] = grid[i][j]
        return res

    def shiftGrid(self, grid, k):
        for _ in range(k):
            grid = self.shiftMatrix(grid)
        return grid

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
z = [[1,2,3],[4,5,6],[7,8,9]]
mesin_hitung = Solution()
print(mesin_hitung.shiftGrid(x, 1))
print(mesin_hitung.shiftGrid(y, 4))
print(mesin_hitung.shiftGrid(z, 9))