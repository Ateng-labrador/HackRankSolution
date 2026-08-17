class Solution:
    def searchInsert(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            m = ((L + R)) // 2
            if nums[m] > target:
                R = m - 1
            elif nums[m] < target:
                L = m + 1
            else:
                return m
        return R + 1

mesin_hitung = Solution()
x = [1, 3, 5, 6]
print(mesin_hitung.searchInsert(x, 5))
print(mesin_hitung.searchInsert(x, 2))
print(mesin_hitung.searchInsert(x, 7))

