class Solution:
    """
    -> 
    """
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # Early Termination
            if nums[i] > 0:
                break
            # To avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two pointer
            L = i + 1
            R = len(nums) - 1
            while L < R:
                m = nums[i] + nums[L] + nums[R]
                if m > 0:
                    R -= 1
                elif  m < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return res
                    

nums = [-1,0,1,2,-1,-4]
mesin_hitung = Solution()
print(mesin_hitung.threeSum(nums))
