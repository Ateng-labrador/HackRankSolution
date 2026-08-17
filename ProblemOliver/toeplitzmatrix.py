"""
Toeplitz Matrix:

Make matrix Toeplitz size n * n


"""
class Solution:
    def ToeplizMatrix(self, start, end):
        res = []
        for i in range(start, end + 1):
            row = []
            for j in range(start, end + 1):
                row.append(i - j)
            res.append(row)
        return res


mesin_hitung = Solution()
x = mesin_hitung.ToeplizMatrix(1, 9)
y = mesin_hitung.ToeplizMatrix(1, 3)
print(y)
