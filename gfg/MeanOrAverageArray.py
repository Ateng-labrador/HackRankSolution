class Solution:
    def findMean(self, arr):
        res = 0
        for i in range(len(arr)):
            res += arr[i]
        return res // len(arr)

mesin_hitung = Solution()
print(mesin_hitung.findMean([1, 3, 4, 2, 6, 5, 8, 7]))
print(mesin_hitung.findMean([4, 4, 4, 4, 4]))
