import sys

sys.set_int_max_str_digits(10000)

class Solution1:
    def addDigit(self, nums: list[int]) -> int:
        n = int("".join(map(str, nums)))
        res = 0
        while n > 0:
            digit = n % 10
            res += digit
            n = n // 10
        return res
    
    def differenceOfSum(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += nums[i]
        return abs(self.addDigit(nums) - res)


class Solution:
    def addDigit(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for i in nums:
            element_sum += i
            while i > 0:
                digit = i % 10
                digit_sum += digit
                i = i // 10
        return abs(element_sum - digit_sum)

mesin_hitung = Solution()
print(mesin_hitung.addDigit([1,15,6,3]))
print(mesin_hitung.addDigit([1,2,3,4]))
