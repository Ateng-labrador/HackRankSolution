class Solution:
    def maximumCount(self, nums):
        pos = 0 
        neg = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                neg += 1
            else:
                continue
        return max(pos, neg)

mesin_hitung = Solution()
x = [-2,-1,-1,1,2,3]
y = [-3,-2,-1,0,0,1,2]
z = [5,20,66,1314]
print(mesin_hitung.maximumCount(x))
print(mesin_hitung.maximumCount(y))
print(mesin_hitung.maximumCount(z))
