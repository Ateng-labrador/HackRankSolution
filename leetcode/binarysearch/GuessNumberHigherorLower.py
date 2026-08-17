class Solution:
    def feasible(mid: int):
        pass

    def guessNumber(self, n):
        L ,R = 1, n
        first_index = -1
        while L <= R:
            m = ((L+R)) // 2
            if first_index > n:
                first_index = m
                R = m - 1
            else:
                L = m + 1
        return first_index
