class Solution:
    def twoSum1(self, numbers, target):
        """
        Brute Force
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                m = numbers[i] + numbers[j]
                if m == target:
                    return [i + 1 , j + 1]
 
    def twoSum(self, numbers, target):
        for i in range(len(numbers) - 1):
            c = target - numbers[i]
            L = i + 1
            R = len(numbers) - 1
            while L <= R:
                m = (L + R) // 2
                if numbers[m] >= c:
                    R = m - 1
                else:
                    L = m + 1            
        return []


nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 4]
t1 = 3
t2 = 6
mesin_hitung = Solution()
print(mesin_hitung.twoSum(nums1, t1))
print(mesin_hitung.twoSum(nums2, t2))
