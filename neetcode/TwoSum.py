class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res

    def twoSum(self, nums, target):
        """
        I don't understand this code
        """
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i

nums1 = [3,4,5,6]
nums2 = [4,5,6]
nums3 = [5,5]
target1 = 7
target2 = 10
target3 = 10
mesin_hitung = Solution()
print(mesin_hitung.twoSum(nums1, target1))
print(mesin_hitung.twoSum(nums2, target2))
print(mesin_hitung.twoSum(nums3, target3))



