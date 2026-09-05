class Solution:
    def getRow(self, rowIndex):
        res = []
        for i in range(rowIndex + 1):
            # ini menyiampakan kanan kiri
            row = [1] * (i + 1)
            for j in range(1, i):
                # menjumlahkan nilai tengah dan menjumlahkn bagian atas dab bawah
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res[rowIndex]
