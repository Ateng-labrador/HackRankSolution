import math

class solution:
    def fakforial(self, n):
        res = 1
        while n > 1:
            res *= n
            n -= 1
        return res 

    def nPr(self, n, r):
        return math.floor((self.fakforial(n) / (self.fakforial(n - r))))

