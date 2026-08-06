class Solution:
    def convertFive(self, n):
        res = []
        if n == 0:
            return 5
        else:
            while n > 0:
                if n % 10 == 0:
                    res.append(5)
                else:
                    res.append(n % 10)
                n = n // 10
            x = list(reversed(res))
            y = int("".join(map(str, x)))
            return y
    