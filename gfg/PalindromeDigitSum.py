class Solution:
    def isDigitSumPalindrome(self, n):
        res = 0
        while n>0:
            res += n % 10
            n = n // 10
        res_str = str(res)
        res_reversed = "".join(reversed(res_str))
        if res_str == res_reversed:
            return True
        else:
            return False

mesin_hitung = Solution()
print(mesin_hitung.isDigitSumPalindrome(56))