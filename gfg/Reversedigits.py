class Solution:
    def reverseDigits(self, n):
        res = []
        while n > 0:
            res.append(n % 10)
            n = n // 10
        return int(''.join(map(str, res)))

mesin_hitung = Solution()
print(mesin_hitung.reverseDigits(200))
print(mesin_hitung.reverseDigits(122))
print(mesin_hitung.reverseDigits(12345))