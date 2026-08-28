"""
Konstruksi Matematis Pembalikan Bilangan

Untuk membentuk R(n) secara aritmatika tanpa mempreosesnya sebagai
teks, gunakan dua operasi dasar berturut - turut:
-> Pengecekan digit terakhir: a_i = N (mod 10)
-> Pembuangan digit terakhir: N <= [N/10]

Prosedur Algoritma:
1. Inisialisasi variabel pembalik R = 0 dan variabel salinan N = n.
2. Selama N > 0,perbarui R dan N:
    R <- (R x 10) + (N (mod 10))
    N <- [N/10]
3, Evaluasi Kondisi akhir:
        Jika sama maka benar jika salah ya salah


"""

class Solution:
    def Palindrome(self, n):
        reverse = 0
        N = n
        while N > 0:
            reverse = (reverse * 10) + (N % 10)
            N //= 10
        return n == reverse

    def reverse(self, n):
        reversed_num = 0
        for i in reversed(str(n)):
            reversed_num = (reversed_num * 10) + int(i)
        return reversed_num

    def isSumPalindrome(self, n):
        if self.Palindrome(n):
            return n

        ite = 0
        N = n
        while ite < 5:
            res = N + self.reverse(N)
            if self.Palindrome(res):
                return res
            else:
                N = res
                ite += 1
        return -1

class SolutionSimpel:
    def reverse(self, n):
        return int(str(n)[::-1])

    def isPalindrome(self, n):
        return str(n) == str(n)[::-1]

    def isSumPalindrome(self, n):
        if self.isPalindrome(n):
            return n

        for _ in range(5):
            n = n + self.reverse(n)
            if self.isPalindrome(n):
                return n
        return -1


mesin_hitung = SolutionSimpel()

