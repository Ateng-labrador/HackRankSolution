class Solution:
    def maximumWealth(self, accounts):
        res = []
        for i in range(len(accounts)):
            res_row = 0
            for j in range(len(accounts[0])):
                res_row += accounts[i][j]
            res.append(res_row)
        return max(res)

    def maximumWealth1(self, accounts):
        res = []
        for i in accounts:
            res.append(sum(i))
        return max(res)

mesin_hitung = Solution()
x = [[1,2,3],[3,2,1]]
y = [[1,5],[7,3],[3,5]]
print(mesin_hitung.maximumWealth1(x))
print(mesin_hitung.maximumWealth1(y))
