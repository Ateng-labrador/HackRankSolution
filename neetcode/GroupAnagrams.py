class Solution:
    def groupAnagrams(self, strs):
        strss = sorted(strs)
        res = []
        for i in range(len(strs)):
            row = []
            for j in range(i + 1, len(strss)):
                if strss[i] == strss[j]:
                    row.append(strss[i])
                    row.append(strss[j])
            res.append(row)
        return res

mesin_hitung = Solution()
print(mesin_hitung.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(mesin_hitung.groupAnagrams(["x"]))
print(mesin_hitung.groupAnagrams([""]))


