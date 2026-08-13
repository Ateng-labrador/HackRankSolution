"""
Code ini berfungsi untuk memperhalus sebuah matrixs/gambar 2D dengan
mengganti nilai setiap piksel menjadi rata - rata dari piksel itu sendiri
beserta tetangga di sekitarnya

leetcode image smotter
"""
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0

                # buat ngecek apakah index berada di sekitarnya
                # penjelajahan area 3 x 3
                for dr in range(-1, 2, 1):
                    for dc in range(-1, 2, 1):
                        # menghitung koordinat calon tetangga
                        nr , nc = r + dr, c + dc

                        # Filter Batas Matriks (Boundart Check)
                        # Memastikan koordinat tetangga tidak berada diluar
                        # matriks(mencegah error index out of range)
                        if 0 <= nr < m and 0 <= nc < n:
                            """
                            Batas Atas/Kiri (0 <= nr): Memastiskan indeks tidak
                            bernilai negatif(tidak keluar dari batas atas matriks)

                            Batas Bawah/Kanan (nr < m): Memastikan tidak lebih dari
                            atau sama dengan jumlah baris m

                            nilai harus berada di antara sama dengan 0 dan kurang 
                            dari batas panjang matriks
                            """
                            total_sum += img[nr][nc]
                            count += 1
                res[r][c] = total_sum // count
        return res
                

if __name__ == "__main__":
    img = [[100,200,100],[200,50,200],[100,200,100]]
    mesin_hitung = Solution()
    print(mesin_hitung.imageSmoother(img))