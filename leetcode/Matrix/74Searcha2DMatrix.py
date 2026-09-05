class Solution:
    def searchMatrix(self, matrix, target):
        """
        -> Pilih Indeks 1D: Algoritma menghitung nilai tengah (m) pada
        rentang batas khayalan 1D.

        -> Terjemahkan ke 2D: saat itu juga, indeks m langsung diubha menggunakna
        rumus menjadi koordinta baris dan kolom untuk melihat angka aslinya dalam matriks

        -> Bandingkan & Potong: Angka asli di koordinat 2d tersebut dicocokkan dengan
        target. Jika lebih besar atau lebih kecil, batas pencarian 1D(L atau R)
        langsung diperbaharui
        """
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = (m * n) - 1
        while L <= R:
            m = (L + R) // 2
            midlle = matrix[m // n][m % n]
            if midlle < target:
                L = m + 1
            elif midlle > target:
                R = m - 1
            else:
                return True
        return False


mesin_hitung = Solution()
print(mesin_hitung.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(mesin_hitung.searchMatrix([[1, 4],[2, 5],], 2))
print(mesin_hitung.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
