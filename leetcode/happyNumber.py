class Solution:
    def sum_digit(self, n: int) -> int:
        res = 0
        while n > 0:
            digit = n % 10
            res += digit * digit
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        set_value = set()
        while True:
            if n == 1:
                return True
            n = self.sum_digit(n)
            if n in set_value:
                return False
            set_value.add(n)
        

mesin_hitung = Solution()
print(mesin_hitung.isHappy(19))