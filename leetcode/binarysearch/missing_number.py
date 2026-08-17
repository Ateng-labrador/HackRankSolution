class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sumtotal = (n*(n + 1)) // 2
        sum_semesta = sum(nums)
        mis = sumtotal - sum_semesta
        return mis

x = [3, 0, 1]
y = [0, 1]
z = [9,6,4,2,3,5,7,0,1]
mesin_hitung = Solution()
print(mesin_hitung.missingNumber(x))
print(mesin_hitung.missingNumber(y))
print(mesin_hitung.missingNumber(z))
