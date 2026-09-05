class Solution:
    def isAnagram(self, s, t):
        s1 = sorted(s)
        t1 = sorted(t)
        return s1 == t1

mesin_hitung = Solution()
print(mesin_hitung.isAnagram("racecar", "carrace"))
print(mesin_hitung.isAnagram("jar", "jam"))
print(mesin_hitung.isAnagram("x", "x"))



