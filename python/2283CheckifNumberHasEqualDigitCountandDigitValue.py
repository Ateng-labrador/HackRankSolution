class Solution:
    def digitCount1(self, num):
        for i in range(len(num)):
            x = num.count(str(i))
            if int(num[i]) != x:
                return False
        return True

    def digitCount(self, num):
        for i in range(len(num)):
            res = 0
            for j in range(len(num)):
                if(num[j] == str(i)):
                    res += 1
                if(res != int(num[i])):
                    return False
        return True

    


# mesin_hitung = Solution()
# print(mesin_hitung.digitCount("1210"))
# print(mesin_hitung.digitCount("030"))

                