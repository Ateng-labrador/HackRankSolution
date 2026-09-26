class Solution:
    def countDigits(self, num):
        res = 0
        for i in str(num):
            if num % int(i) == 0:
                res += 1
        return res

mesin_hitung = Solution()
print(mesin_hitung.countDigits(7))
print(mesin_hitung.countDigits(121))
print(mesin_hitung.countDigits(1248))
                
        