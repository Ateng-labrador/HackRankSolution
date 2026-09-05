class Solution:
    def searchMatrix1(self, matrix, target):
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

    def searchMatrix2(self, matrix, target):
        for i in range(len(matrix)):
            num = matrix[i]
            L = 0
            R = len(num) - 1
            while L <= R:
                m = (L + R) // 2
                if num[L] > num[R]:
                    return False
                elif num[R] < target:
                    break
                elif num[m] > target:
                    R = m - 1
                elif num[m] < target:
                    L = m + 1
                else:
                    return True
            return False

    def searchMatrix3(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        L = 0
        R = (row * col) - 1
        while L <= R:
            m = (L + R) // 2
            idx = matrix[m//col][m % col]
            if idx < target:
                L = m + 1
            elif idx > target:
                R = m - 1
            else:
                return True
        return False

    def searchMatrix2(self, matrix, target):
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
print(mesin_hitung.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(mesin_hitung.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
