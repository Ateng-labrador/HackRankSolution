class Solution:
    def containsNearbyDuplicate1(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        index = {}
        for i, j in enumerate(nums):
            if j in index and  i - index[j] <= k:
                return True
            index[j] = i
        return False


        

mesin_hitung = Solution()
x1 = [1,2,3,1]
x2 = [1,0,1,1]
x3 = [1,2,3,1,2,3]
print(mesin_hitung.containsNearbyDuplicate(x1, 3))
print(mesin_hitung.containsNearbyDuplicate(x2, 1))
print(mesin_hitung.containsNearbyDuplicate(x3, 2))
