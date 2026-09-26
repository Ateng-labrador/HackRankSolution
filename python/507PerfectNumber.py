class Solution:
    def checkPerfectNumber1(self, x):
        # TLX
        res = []
        for i in range(x-1, 0,-1):
            if x % i == 0:
                res.append(i)
        return sum(res) == x

    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        res = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                res.append(i)
                if i != num // i:
                    res.append(num//i)
        return sum(res) == num

mesin_hitung = Solution()
print(mesin_hitung.checkPerfectNumber(28))
print(mesin_hitung.checkPerfectNumber(7))
