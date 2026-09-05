class Solution:
    def searchMatrix(self, matrix, target):
        for i in matrix:
            L = 0
            R = len(i) - 1
            while L <= R:
                m = (L + R) // 2
                if i[m] > target:
                    R = m - 1
                elif i[m] < target:
                    L = m + 1
                else:
                    return True
        return False
            

x = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
mesin_hitung = Solution()
y = mesin_hitung.searchMatrix(x, 10)
print(y)
