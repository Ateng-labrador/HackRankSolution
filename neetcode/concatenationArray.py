class Solution:
    def hasDuplicate1(self, nums):
        # salah
        L = 0
        R = len(nums) - 1
        while L <= R:
            m = (L + R) // 2
            if nums[m] > nums[m]:
               L = m + 1
            elif nums[m] < nums[m]:
                R = m - 1
            else:
                return True
        return False

    def hasDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i- 1]:
                return True
        return False

mesin_hitung = Solution()
print(mesin_hitung.hasDuplicate([1, 2, 3, 3]))
print(mesin_hitung.hasDuplicate([1, 2, 3, 4]))

