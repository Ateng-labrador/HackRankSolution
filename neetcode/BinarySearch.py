class Solution:
    def search(self, nums, target):
        L = 0
        R = len(nums) - 1
        while L <= R:
            m = (L + R) // 2
            if nums[m] > target:
                R = m - 1
            elif nums[m] < target:
                L = m + 1
            else:
                return m
        return -1

mesin_hitung = Solution()
print(mesin_hitung.search([-1,0,2,4,6,8], 4))
print(mesin_hitung.search([-1,0,2,4,6,8], 3))
