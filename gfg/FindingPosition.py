class Solution:
    def nthPosition(self, n):
        res = []
        for i in range(2, n + 1):
            if i % 2 == 0:
                res = i
        return res

mesin_hitung = Solution()
print(mesin_hitung.nthPosition(5))
print(mesin_hitung.nthPosition(9))
