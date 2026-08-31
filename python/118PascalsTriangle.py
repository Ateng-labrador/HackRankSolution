"""
Make the pascal

1. Start with the first row: Create a list containing [1]
2. Loop for each new row: For row i, start a new row that begins with 1.
3. Calculate middle numbers: Add adjacent pairs of numbers from the previous row
4. End the row: Add 1 to the end of the new row
5. Save and repeat:
"""


class Solution:
    def generate(self, numRows):
        triangle = [[1]]
        for i in range(numRows - 1):
            current_row = [1]
            previous_row = triangle[-1]
            for j in range(len(previous_row) - 1):
                current_row.append(previous_row[j] + previous_row[j + 1])
            current_row.append(1)
            triangle.append(current_row)
        return triangle


    def generate_pascal(self, numRows):
        res = []
        for i in range(numRows):
            # Membuat baris sementara yang isinya angka 1 semua.Ini langkah
            # otomatis memastikan ujung kiri dan kanan segitiga selalu bernilai 1
            row = [1] * (i + 1)
            for j in range(1, i):
                # mengambil dua angka yang letaknya bersebleahan dari baris
                # tepat diatasnya (res[i-1])
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res


class Solution1:
    def make_pascal(self, numRows):
        res = []
        for i in range(numRows + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res[numRows]

    # def take_pascal(self, n):
    #     res = self.take_pascal(n)
    #     print(res[n])

mesin_hitung = Solution1()
print(mesin_hitung.make_pascal(3))
print(mesin_hitung.make_pascal(0))
print(mesin_hitung.make_pascal(1))
