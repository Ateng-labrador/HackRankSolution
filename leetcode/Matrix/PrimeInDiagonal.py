import math

class Solution:
    def checkPrimes(self, nums):
        if nums < 2:
            return False
        if nums == 2:
            return True
        if nums % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(nums)) + 1, 2):
             if nums % i == 0:
                  return False
        return True

    def diagonalPrime(self, nums):
        n = len(nums)
        max_prime = 0
        for i in range(n):
            val1 = nums[i][i]
            val2 = nums[i][n - 1 - i]
            if val1 > max_prime and self.checkPrimes(val1):
                max_prime = val1
            if val2 > max_prime and self.checkPrimes(val2):
                max_prime = val2
        return max_prime


mesin_hitung = Solution()
x = [[1,2,3],[5,6,7],[9,10,11]]
y = [[1,2,3],[5,17,7],[9,11,10]]
print(mesin_hitung.diagonalPrime(x))
print(mesin_hitung.diagonalPrime(y))

