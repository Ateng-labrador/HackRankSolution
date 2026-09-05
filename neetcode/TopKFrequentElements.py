class Solution:
    def topKFrequent(self, nums, k):
        res = set()
        f = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if f <k:
                    if nums[i] == nums[j] and (nums[i] and nums[j] not in res):
                        res.add(nums[i])
                        f += 1
        return list(res)

    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get

mesin_hitung = Solution()
print(mesin_hitung.topKFrequent([1,2,2,3,3,3], 2))
print(mesin_hitung.topKFrequent([1,1,1,2,2,3], 2))
print(mesin_hitung.topKFrequent([7, 7], 1))
