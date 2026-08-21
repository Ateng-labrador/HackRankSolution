import math

class Solution:
    def arrangeCoins(self, n):
        return (-1 + math.sqrt(1 + 8 * n)) // 2
            

mesin_hitung = Solution()
mesin_hitung.arrangeCoins(8)
