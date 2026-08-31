import math

class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        res = [True] * (n + 1)
        res[0] = False
        res[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if res[i]:
                for j in range(i*i, n + 1, i):
                    res[j] = False

        # Time Limited
        resf = 0
        for i in range(2, n + 1):
            if res[i] == True:
                resf += 1
        return resf

    def countPrimes(self, n):
        if n < 2:
            return 0

        res = [True] * (n + 1)
        res[0] = res[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if res[i]:
                for j in range(i*i, n + 1, i):
                    res[j] = False
        return sum(res[2:n])
    
                

mesin_hitung = Solution()
print(mesin_hitung.countPrimes(3))
