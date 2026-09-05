class Solution:
    def Palindrome(self, s):
            r = ""
            for i in s:
                r = i + r
            return r == s

    def Palindrome1(self, s):
        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    
    def isPalindrome(self, s):
        x = "".join(i.lower() for i in s if i.isalnum())
        return self.Palindrome1(x)

    
s1 = "Was it a car or a cat I saw?"
s2 = "tab a cat"
mesin_hitung = Solution()
print(mesin_hitung.isPalindrome(s1))
print(mesin_hitung.isPalindrome(s2))

