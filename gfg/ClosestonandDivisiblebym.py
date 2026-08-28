# skip

class Solution1:
    def closestNumber(self, n, m):
        q = n // m
        n1 = m * q
        if (n * m) > 0:
            n2 = m * (q + 1)
        else:
            m * (q - 1)

        if abs(n - n1) < abs(n - n2):
            return n1
        elif abs(n - n1) > abs(n - n2):
            return n2
        else:
            if abs(n1) > abs(n2):
                return n1
            else:
                return n2

class Solution:
    def closestNumber(self, n, m):
        pass

