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

    def mySqrt1(self, x):
        """
        Solusi 69 sqrt(x)
        cara kerja code ini

        x = 9
        iterasi ke - 1
            L, R = 1, 4
            m = 2
            sqrt = 4
            4 < 9
            L = 2 + 1 = 3
        iterasi ke - 2
            L, R = 3, 4
            m = 7 // 2 = 3
            sqrt = 9
            return 9

            
        x = 8
        iterasi ke - 1
            L, R = 1, 4
            m = 2
            sqrt = 4
            4 < 8
            L = 2 + 1 = 3
        iterasi ke - 2
            L, R = 3, 4
            m = 3
            sqrt = 9
            9 > 8
            R = 3 - 1 = 2
        karna perulangan  berhenati makanya R = 2
        """
        if x < 2:
            return x
        L = 1
        R = x // 2
        while L <= R:
            m = (R + L) // 2
            sqrt = m * m
            if sqrt > x:
                R = m - 1
            elif sqrt < x:
                L = m + 1
            else:
                return m
        return R




mesin_hitung = SolutionBruteOFrce()
mesin_hitung1 = Solution()
print(mesin_hitung1.mySqrt(4))
print(mesin_hitung.mySqrtloop(4))

