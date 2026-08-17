"""
convolution:

"""
class Solution:
    def convolution(self, in1, in2):
        n, m = len(in1), len(in2)
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += in1[i]*in2[j]
        return res

mesin_hitung = Solution()
print(mesin_hitung.convolution())
        