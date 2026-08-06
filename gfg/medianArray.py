class Solution:
    def median(self, arr):
        x = sorted(arr)
        indekx_kiri = (len(x)//2) -1
        indekx_kanan = (len(x)//2)
        if len(x) % 2 == 0:
            return (x[indekx_kiri] + x[indekx_kanan])/2
        else:
            return x[len(x)//2]
