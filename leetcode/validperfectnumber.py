class Solution:
    def isPerfectSquare(self, num):
        L = 1
        R = num // 2
        while L <= R:
            m = (L + R) // 2
            sqrt = m * m
            if sqrt > num:
                R = m - 1
            elif sqrt < num:
                L = m + 1
            else:
                return True
        return False

mesin_hitung = Solution()
print(mesin_hitung.isPerfectSquare(16))
print(mesin_hitung.isPerfectSquare(14))
