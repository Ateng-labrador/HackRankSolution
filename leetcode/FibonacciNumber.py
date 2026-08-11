class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        res = [0, 1]

        for _ in range(2, n):
            # res[-1] mundur satu langkah
            # res[-2] mundur dua langkah
            res.append(res[-1] + res[-2])
        return res[n - 1] + res[n - 2]

mesin_hitung = Solution()
print(mesin_hitung.fib(4))