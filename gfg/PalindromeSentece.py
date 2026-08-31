"""
1. Teks harus tetap di proses sebagai teks(string)
    x = "".join(s.split()) hanya menghapus spasi dan
    membiarkan huruf besar/kecil serta tanda baca.

    isalnum()
    
"""

# Algoritma to check Palindrome String

class Solution:
    def checkPalindrome1(self, s):
        r = ""
        for char in s:
            r = char + r
        return r == s

    def checkPalindrome2(self, s):
        L = len(s)
        for i in range(L // 2):
            if s[i] != s[L - i - 1]:
                return False
        return True

    def checkPalindrome(self, s):
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    def isPalinSent(self, s):
        x = "".join(i.lower() for i in s if i.isalnum())
        return self.checkPalindrome(x)


mesin_hitung = Solution()
print(mesin_hitung.isPalinSent("Too hot to hoot"))
print(mesin_hitung.isPalinSent("Abc 012..## 10cbA"))
print(mesin_hitung.isPalinSent("ABC $. def01ASDF"))

