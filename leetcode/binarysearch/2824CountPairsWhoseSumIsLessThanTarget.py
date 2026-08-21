class Solution:
    def countPairs(self, nums, target):
        nums.sort()
        res = 0
        L = 0
        R = len(nums) - 1
        while L < R:
            if nums[L] + nums[R] < target:
                res += (R - L)
                L += 1
            else:
                R -= 1
        return res

    def countPairs1(self, nums, target):
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1
        return res

"""
Logika dalam soal ini karna 1 + 4 saja sudah avalid (kurang dari 6)
maka 2 jika dipasangkan dengan semua angka di sebelah kri 4 pasti
valid juga.

Soal ini meminta kita untuk mencari jumlah pasangan yang kurang dari target
"""


nums = [-1, 1, 2, 3, 1]
nums1 = [-6,2,5,-2,-7,-1,3]
mesin_hitung = Solution()
print(mesin_hitung.countPairs1(nums, 2))
# 
print(mesin_hitung.countPairs1(nums1, -2))


