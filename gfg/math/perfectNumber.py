class Solution:
    def factorial(self, N):
        if N <= 1:
            return 1
        else:
            return N * self.factorial(N - 1)

    def isPerfect(self, N):
        x = [int(i) for i in str(N)]
        res = 0
        for i in x:
            res += self.factorial(i)
        if res != N:
            return 0
        else:
            return 1
