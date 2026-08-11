class Solution:
    def tribonacci(self, n: int) -> int:
        if n<= 0:
            return 0
        elif n == 1:
            return 0
        fib = [0, 1, 1]
        for _ in range(3, n):
            fib.append(fib[-1] + fib[-2] + fib[-3])
        return fib[n - 1] + fib[n - 2] + fib[n - 3] 

mesin_hitung = Solution()
print(mesin_hitung.tribonacci(3))
print(mesin_hitung.tribonacci(4))
print(mesin_hitung.tribonacci(5))
print(mesin_hitung.tribonacci(6))