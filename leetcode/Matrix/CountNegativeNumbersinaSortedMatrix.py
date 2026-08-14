class Solution:
    def countNegatives(self, grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    res += 1
        return res

mesin_hitung = Solution()
x = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
y = [[3,2],[1,0]]
print(mesin_hitung.countNegatives(x))
print(mesin_hitung.countNegatives(y))