"""
ugly number


An ugly number is defined as a positive integer whose only prime
factors are 2, 3, and 5.In other word, when you break down the number into
its prime factorization, it should only contain the primes 2, 3,and 5
(or no prime factors at all, which would be the number 1)
"""


class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False

        factor = [2, 3, 5]
        for i in factor:
            while n % i == 0:
                n //= i
        return n == 1

    def isUgly(self, n):
        if n <= 0:
            return False

        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True

mesin_hitung = Solution()
print(mesin_hitung.isUgly1(6))
print(mesin_hitung.isUgly1(1))
print(mesin_hitung.isUgly1(14))