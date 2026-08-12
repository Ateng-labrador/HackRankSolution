class Solution:
    def sumDigit(self, n: int) -> int:
        res = 0
        while n > 0:
            digit = n % 10
            res += digit
            n = n // 10
        return res

    def addDigits(self, num: int) -> int:
        num = self.sumDigit(num)
        while num >= 10:
            num = self.sumDigit(num)
        return num
            

mesin_hitung = Solution()
print(mesin_hitung.addDigits(19))
