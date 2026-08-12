class Solution1:
    def arrayPairSum(self, nums: list[int]) -> int:
        left = len(nums) // 2 
        left1 = [nums[i] for i in range(left)]
        right1 = [nums[i] for i in range(left, len(nums))]
        return min(left1) + min(right1)
        

class Solution:
    def arrayPairSum(self, nums list[int]) -> int:
        pass