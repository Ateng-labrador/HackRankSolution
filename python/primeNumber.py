import math

# A number is only proven prime if it fails to divide by all numbers
"""
Faktor pembagi selalu datang berpasangan

Jika sebuah angka memiliki pembagi yang lebih besar dari akar kuadratnya,
maka pasangan dari pembagi tersebut pastilah anga yang lebih kecil dari
akar kuadratnya.

"""


class CheckPrimeNumber:
    def naivAlgo(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def devOpti(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def Sieveoferatosthenes(self, n):
        if n < 2:
            return False

        A = [True] * (n + 1)
        A[0] = False
        A[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if A[i]:
                for j in range(i*i, n + 1, i):
                    A[j] = False
        return True


class MakePrimeNumber:
    def NaivAlgor(self, n):
        check_prime = CheckPrimeNumber()

        if n < 2:
            return []

        res = []
        for i in range(2, n + 1):
            if check_prime.naivAlgo(i):
                res.append(i)
        return res

    def SieveOferatosthenes(self, n):
        check_prime = CheckPrimeNumber()
        res = []
        if n < 2:
            return []
        for i in range(2, n + 1):
            if check_prime.Sieveoferatosthenes(n):
                res.append(i)
        return res


mesin_hitung = CheckPrimeNumber()
mesin_print = MakePrimeNumber()
# print(mesin_print.NaivAlgor(11))
print(mesin_print.SieveOferatosthenes(10))
# print(mesin_hitung.devOpti(11))
# print(mesin_hitung.naivAlgo(11))
# print(mesin_hitung.Sieveoferatosthenes(15))

