class Solution:
    def findBigNumber(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = [max(matrix[r][c] for r in range(m)) for c in range(n)]
        return max(res)

    def findSmallNumber(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = [min(matrix[r][c] for r in range(m)) for c in range(n)]
        return min(res)

    def findLuckyNumber(self, matrix: list[list[int]]) -> list[int]:
        """
        Karena matriks di python berbentuk matrix[baris][kolom], mengambil
        elemen satu baris itu mudah(matrix[i]), tapi untuk mengambil elemen satu
        kolom berarti harus memegang indeks kolomnya dan mengecek ke bawah.

        sehingga ubah kolom menjadi baris.
        """
        minList = []
        maxList = []

        # row(baris)
        for i in matrix:
            minList.append(min(i))
        # column(kolom)
        for j in range(len(matrix[0])):
            column_elements = [matrix[i][j] for i in range(len(matrix[0]))]
            maxList.append(max(column_elements))
        for num in maxList:
            if num in minList:
                return [num]

    def findLuckyNumber1(self, matrix: list[list[int]]) -> list[int]:
        minRow = {min(r) for r in matrix}
        maxRow = {max(c) for c in zip(*matrix)}
        return list(minRow & maxRow)

matrix = [[3,7,8],[9,11,13],[15,16,17]]
mesin_hitung = Solution()
print(mesin_hitung.findLuckyNumber1(matrix))
