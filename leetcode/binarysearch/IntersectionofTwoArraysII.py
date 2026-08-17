class Solution:
    def intersect(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

num1 = [1,2,2,1]
num2 = [2, 2]
num11 = [4,9,5]
num22 = [9,4,9,8,4]
mesin_hitung = Solution()
print(mesin_hitung.intersect(num1, num2))
print(mesin_hitung.intersect(num11, num22))
