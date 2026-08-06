import math

# karna yang diminta angka perfect number di bawah n, yang dimana n
# adalah bilangan kuadrat sempurna juga

class Solution:
    def countSquates(self, n):
        return int(math.sqrt(n - 1))

mesin_hitung = Solution()
print(mesin_hitung.countSquates(9))
print(mesin_hitung.countSquates(3))