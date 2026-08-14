class Solution:
    def search(self, nums, t):
        """
        time kompleksitas o(n)
        """
        pos = 0 
        for i in range(len(nums)):
            if nums[i] == t:
                pos = i
                break
        if pos != 0:
            return pos
        else:
            return -1
    def search1(self, nums, t):
        L = 0
        R = len(nums) - 1
        while L <= R:
            m = L + ((R - L) // 2)
            if nums[m] > t:
                R = m - 1
            elif nums[m] < t:
                L = m + 1
            else:
                return m
        return -1



mesin_hitung = Solution()
x = [-1,0,3,5,9,12]
y = [-1,0,3,5,9,12]
print(mesin_hitung.search(x, 9))
print(mesin_hitung.search(y, 2))