class Solution:
    def searchMatrix1(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = (m * n) - 1
        while L <= R:
            m = (L + R) // 2
            idx = matrix[m // n][m % n]
            if idx > target:
                R = m - 1
            elif idx < target:
                L = m + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = n - 1
        while((L < m) and R >= 0):
            if matrix[L][R] > target:
                R -= 1
            elif matrix[L][R] < target:
                L += 1
            else:
                return True
        return False

mesin_hitung = Solution()
x1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
x2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(mesin_hitung.searchMatrix([[1, 4],[2, 5]], 2))
print(mesin_hitung.searchMatrix(x1, 5))
print(mesin_hitung.searchMatrix(x2, 20))