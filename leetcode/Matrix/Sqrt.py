class Solution:
    def mySqrt1(self, x):
        """
        Boros memori
        """
        if x < 2:
            return x
        res = [i*i for i in range(x)]
        L = 0
        R = len(res) - 1

        while L <= R:
            m = (R + L) // 2
            if res[m] > x:
                R = m - 1
            elif res[m] < x:
                L = m + 1
            else:
                return m
        return R
    
    def mySqrt2(self, x):
        """
        return m (di dalam loop) -> dipakai jika angka x memilki akar pas
        bulat

        return R (di dipakai jika akar x adalah angka desimal, untuk mengambil
        )nilai bulat dibawahnya.
        """
        if x < 2:
            return x
        L = 1
        # Akar dari x tidak pernah lebih besar dari x // 2
        R = x // 2
        while L <= R:
            m = (L + R) // 2
            sqr = m * m
            if sqr > x:
                R = m - 1
            elif sqr < x:
                L = m + 1
            else:
                return m
        return R


mesin_hitung = Solution()
print(mesin_hitung.mySqrt2(4))
print(mesin_hitung.mySqrt2(8))
