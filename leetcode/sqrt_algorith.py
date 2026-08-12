class SolutionBruteOFrce:
    def mySqrtWhile(self, x: int) -> int :
        i = 0
        while i * i <= x:
            i += 1
        return i - 1
    def mySqrtloop(self, x: int) -> int:
        # dikurangi 1 karena perulangan berhenti saat i * i sudah > x
        for i in range(x + 2):
            if i * i > x:
                return i - 1
        return 0


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - 1) // 2)
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m
        return r


mesin_hitung = SolutionBruteOFrce()
mesin_hitung1 = Solution()
print(mesin_hitung1.mySqrt(4))
print(mesin_hitung.mySqrtloop(4))

