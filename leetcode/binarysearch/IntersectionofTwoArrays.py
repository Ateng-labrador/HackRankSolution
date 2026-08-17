class Solution:
    def intersection1(self, num1, num2):
        return list(set(num1) & set(num2))

    def intersection(self, num1, num2):
        a = set(num1)
        b = set(num2)
        return list(a & b)

x = [1,2,2,1]
y = [2,2]
x1 = [4,9,5]
y2 = [9,4,9,8,4]

mesin_hitung = Solution()
print(mesin_hitung.intersection(x, y))
print(mesin_hitung.intersection(x1, y2))
