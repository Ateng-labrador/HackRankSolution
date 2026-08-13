"""
looping di balik


for i in range(x, -1, -1, -1):
    for j in range(y, -1, -1, -1):

    looping ini mengambil nilai array membaca nilai
    dari kanan ke kiri.Tapi jika tujuannya untuk melakukan flip
    matriks.

    for i in range(len(image)):
        for j in range(len(image[0])):
            res[i][j] = image[i][len(image[0]) - 1 - j]
"""



class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = [[0 for _ in range(len(image))] for _ in range(len(image[0]))]

        for i in range(len(image)):
            for j in range(len(image[0])):
                res[i][j] = image[i][len(image[0]) - 1 - j]

        resF = []
        for i in range(len(image)):
            row = []
            for j in range(len(image[0])):
                if res[i][j] == 0:
                    row.append(1)
                elif res[i][j] == 1:
                    row.append(0)
                else:
                    row.append(res[i][j])
            resF.append(row)
        return resF

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Looping ini mengambil setiap element baris di image

        sehingga ketika baris - 0.misal
        [1,1,0] maka menjadi [0, 1, 1]
        """
        for row in image:
            row.reverse()
            for i in range(len(row)):
                """
                cara jerdik untuk mengganti nilai nol menjadi 1 atau 0
                """
                row[i] = 1 - row[i]
        return image


x = [[1,1,0],[1,0,1],[0,0,0]]
y = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# mesin_hitung = Solution()
# print(mesin_hitung.flipAndInvertImage(x))
# print(mesin_hitung.flipAndInvertImage(y))
