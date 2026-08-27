class Solution:
    def mergeTwoLists(self, list1, list2):
        res = list1 + list2
        n = len(res)
        while n > 1:
            newn = 0
            for i in range(1, n):
                if res[i - 1] > res[i]:
                    (res[i - 1], res[i]) = (res[i], res[i - 1])
                    newn = i
            n = newn
        return res

mesin_hitung = Solution()
x = []
y = [0]
print(mesin_hitung.mergeTwoLists(x, y))
