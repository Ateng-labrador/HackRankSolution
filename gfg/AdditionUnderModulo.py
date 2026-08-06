class Solution:
    def sumUnderModulo(self, a, b, M):
        return (a + b) % M

mesin_hitung = Solution()
print(mesin_hitung.sumUnderModulo(10, 20, 3))
print(mesin_hitung.sumUnderModulo(100, 13, 107))
