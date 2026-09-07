class Matrix_oprek:
    def matriks_pascal_oprek(self, matriks):
        res = []
        for i in range(len(matriks)):
            for j in range(len(matriks[0])):
                x = matriks[i - 1][j - 1] + matriks[i - 1][j]
            res.append(x)
        return res

    def print_matriks_operek(self, matriks):
        y = self.matriks_pascal_oprek(matriks)
        for i in y:
            print(i)


class Matriks_salib:
    def sum_diagonal(self, matriks):
        res = 0
        res1 = 0
        for i in range(len(matriks)):
            res += matriks[i][i]

        for j in range(len(matriks)):
            print(matriks[j][len(matriks) - 1 - j])





mesin_hitung = Matrix_oprek()
mesin_hitung1 = Matriks_salib()
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(x)
# print(mesin_hitung1.sum_diagonal(x))
# print(mesin_hitung.matriks_pascal_oprek(x))
print(x[-1][-1])
print(x[-3][-3])


