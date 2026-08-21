# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n 
        while (L < R):
            m = (L + R) // 2
            if isBadVersion(m):
                R = m
            else:
                L = m + 1
        return L
