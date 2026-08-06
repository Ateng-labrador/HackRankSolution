class Solution:
    def sumOfAP(self, n, a, d):
        res = 0
        for i in range(n):
            res += a + i * d
        return res

mesin_hitung = Solution()
print(mesin_hitung.sumOfAP(3, 1, 2))
