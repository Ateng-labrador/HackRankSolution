class Solution1:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        hasil = set()

        left = 0
        right = len(nums) - 1

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            hasil.add(avg)
            left += 1
            right -= 1
        return len(hasil)


class Solution2:
    def distinctAverages(self, nums: list[int]) -> int:
        sums = set()
        nums.sort()

        for i in range(len(nums) // 2):
            sums.add(nums[i] + nums[len(nums) - 1 - i])
        return len(sums)


if __name__ == "__main__":
    nums = [10,2,2,0,4,0]
    mesin_hitung = Solution1()
    print(mesin_hitung.distinctAverages(nums))
    
