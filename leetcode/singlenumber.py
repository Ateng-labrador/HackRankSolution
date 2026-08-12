# Bit manipulation
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


mesin_hitung = Solution()
print(mesin_hitung.singleNumber([2, 2, 1]))
print(mesin_hitung.singleNumber([4,1,2,1,2]))
print(mesin_hitung.singleNumber([1]))
