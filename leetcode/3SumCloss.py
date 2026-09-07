class Solution:
    def threeSumClosest1(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            L = i + 1
            R = len(nums) - 1

            while L < R:
                m = nums[i] + nums[L] + nums[R]
                if abs(m - target) < abs(closest_sum - target):
                    closest_sum = m
                if m > target:
                    R -= 1
                elif m < target:
                    L += 1
                else:
                    return m
        return closest_sum

    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            L = i + 1
            R = len(nums) - 1
            while L < R:
                m = nums[i] + nums[L] + nums[R]
                if abs(target - m) < abs(ans - m):
                    ans = m
                if m > target:
                    R -= 1
                else:
                    L += 1
            return ans

mesin_hitung = Solution()
print(mesin_hitung.threeSumClosest1([-1,2,1,-4], 1))
print(mesin_hitung.threeSumClosest1([0, 0, 0], 1))
print(mesin_hitung.threeSumClosest1([0, 1, 2], 3))

                
                