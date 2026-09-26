class Solution:
    def proto(self, x):
        for i in str(x):
            if x % int(i) != 0:
                return False
        return True

    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right+1):
            mark = True
            for j in str(i):
                if j == '0' or i % int(j) != 0:
                    mark = False
                    break
            if mark:
                res.append(i)
        return res

mesin_hitung = Solution()
print(mesin_hitung.selfDividingNumbers(1, 22))
print(mesin_hitung.selfDividingNumbers(47, 85))
            
