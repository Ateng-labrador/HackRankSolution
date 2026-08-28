class Solution:
    def faktorial(self, n):
        if n <=1:
            return 1
        else:
            return n * self.faktorial(n - 1)

    def isStrong(self, n):
        sam = [int(x) for x in str(n)]
        res = 0
        for i in sam:
            res += self.faktorial(i)
        if res == n:
            return True
        else:
            return False


x = 145
y = 5314
mesin_hitung = Solution()
print(mesin_hitung.isStrong(x))
print(mesin_hitung.isStrong(y))

