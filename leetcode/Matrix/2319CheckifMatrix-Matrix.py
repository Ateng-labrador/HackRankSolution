class Solution:
    def checkXMatrix(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j or i + j == len(grid) - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True

mesin_hitung = Solution()
grid1 = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
grid2 = [[5,7,0],[0,3,1],[0,5,0]]
print(mesin_hitung.checkXMatrix(grid1))
print(mesin_hitung.checkXMatrix(grid2))
