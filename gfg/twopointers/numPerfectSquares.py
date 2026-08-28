import math

class Solution:
    def numOFPerfectSquares(self, a, b):
        """
        Untuk menentukan jumlah bilangan kuadrat sempurna dalam rentang
        tertutup [a, b], perlu untuk menghitung banyaknya bilangan bulat
        k yang memenuhi pertidaksamaan


        a <= k^2 <= b

        dengan menarik akar kuadrat pada seluruh ruas (a, b>= 1):

        sqrt(a) <= k <= sqrt(b)

        banyak bilangan bulat k yang berada di dalam rentang tersebut 
        di rumuskan secara matematis:

        [sqrt(b)] - [sqrt(a - 1)]
        """
        return math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1))


mesin_hitung = Solution() 
print(mesin_hitung.numOFPerfectSquares(3, 8))
print(mesin_hitung.numOFPerfectSquares(9, 25))