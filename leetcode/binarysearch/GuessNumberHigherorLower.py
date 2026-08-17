class Solution:
    def guessNumber(self, n):
        def feasible(mid):
            pass
        L ,R = 1, n
        first_index = -1
        while L <= R:
            m = ((L+R)) // 2
            if feasible(m):
                first_index = m
                R = m - 1
            else:
                L = m + 1
        return first_index
