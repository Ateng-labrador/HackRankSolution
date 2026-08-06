class Solution:
    def isSumPalindrome(self, n):
        x = n
        res = []
        while x > 0:
            res.append(x % 10)
            x = x // 10
        r = n + int(''.join(map(str, res)))
        r1 = list(map(int, str(r)))
        if list(reversed(r1)) == r1:
            return r
        else:
            return -1


mesin_hitung = Solution()
print(mesin_hitung.isSumPalindrome(23))
