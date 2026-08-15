"""
Fungsi zip() dalam python adalah fungsi bawaan (built-in) yang digunakan
untuk menggabungkan dua atau lebih data yang bisa di-loop (iterable)

zip bagaikan pada jaket: gigi kiri dan gigi kanan dipasangkan satu per satu
dari atas ke bawah.

cara kerja zip()

zip() mengambil elemen pertama dari setiap data, menggabungkan menjadi sebuah
tuple, lalu lanjut ke elemen kedua, ketiga, dan seterusnya

hasil dari zip adalah sebuah iterator/zip

-> contoh penggunaan menggabungkan dua list
-> looping beberapa list secara bersamaan
-> membuat dictionary dengan cepat
-> unzipping (membuka pasangan)

"""
class Solution:
    def findRotation(self, mat, target):
        rot = 4
        n = 0
        mat = mat
        while n <= rot:
            if mat != target:
                matRot  = [list(x) for x in zip(*mat[::-1])]
                n += 1
                mat = matRot
            else:
                return True
        return False

    def rotate(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for i in range(n):
            mat[i].reverse()
        return mat

    def findRot(self, mat, target):
        for _ in range(4):
            if mat != target:
                mat = self.rotate(mat)
            else:
                return True
        return False


x = [[0,0,0],[0,1,0],[1,1,1]]
y = [[1,1,1],[0,1,0],[0,0,0]]
z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mesin_hitung = Solution()
print(mesin_hitung.findRot(x, y))


