class Solution:
    def satisfiesConditionsfail(self, grid):
        if len(grid[0]) == 1 and len(grid) == 1:
            return True
        if len(grid[0]) == 1:
            return False
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                x = grid[i][j] == grid[i + 1][j]
                y = grid[i][j] != grid[i][j + 1]
                if x and y:
                    return True
                else:
                    return False


    def satisfiesConditionsfailagain(self, grid):
        resHor = [i for i in zip(*grid)]
        if len(grid[0]) == 1 and len(grid) == 1:
            return True
        if len(grid[0]) == 1:
            return False
        check1 = False
        check2 = False
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                x = grid[i][j] == grid[i + 1][j]
                if x:
                    check1 = True
                else:
                    check1 = False
        for i in range(len(resHor) - 1):
            for j in range(len(resHor[0]) - 1):
                x = resHor[i][j] != resHor[i][j + 1]
                if x:
                    check2 = True
                else:
                    check2 = False
        return check1 == check2
    """
    Dengan enumerate(), kamu bisa mendapatkan indeks dan nilai (values)
    dari list tersebut bersamaan tanpa harus repor membuat variabel penghitung
    manual
    """

    def satisfiesConditions(self, grid):
        for i, j in enumerate(grid):
            for k, l in enumerate(j):
                if i + 1 < len(grid) and l != grid[i + 1][k]:
                    return False
                if k + 1 < len(grid[0]) and l == grid[i][k + 1]:
                    return False
        return True
                

        

mesin_hitung = Solution()
x = [[1,0,2],[1,0,2]]
y = [[1,1,1],[0,0,0]]
z = [[1],[2],[3]]
print(mesin_hitung.satisfiesConditions(x))
print(mesin_hitung.satisfiesConditions(y))
print(mesin_hitung.satisfiesConditions(z))
