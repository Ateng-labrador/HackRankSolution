class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        res = 0
        x = sorted(nums)
        for i in range(len(x)-1):
            if x[i] == x[i + 1]:
                res += 1
        if res != 0:
            return True
        return False

    def containsSuplicate1(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



mesi_hitung = Solution()
x1 = [1,2,3,1]
x2 = [1, 2,3, 4]
x3 = [1,1,1,3,3,4,3,2,4,2]
print(mesi_hitung.containsDuplicate(x1))
print(mesi_hitung.containsDuplicate(x2))
print(mesi_hitung.containsDuplicate(x3))
