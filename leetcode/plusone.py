class Solution:
    def plusone(self, digits: list[int]) -> list[int]:
        x = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(x)]

mesin_hitung = Solution()
print(mesin_hitung.plusone([1,2, 3]))
        