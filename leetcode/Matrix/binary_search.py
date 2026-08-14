class BinarySearch:
    def binary_search(self, A, T):
        L = 0
        R = len(A) - 1
        while L <= R:
            m = L + ((R - L) // 2)
            # m = (L + R) // 2
            if A[m] < T:
                L = m + 1
            elif A[m] > T:
                R = m - 1
            else:
                return m
        return "Gak Ada"


A = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
mesin_hitung = BinarySearch()
print(mesin_hitung.binary_search(A, 9))
