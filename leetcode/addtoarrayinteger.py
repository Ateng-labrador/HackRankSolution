class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        x = int("".join(map(str, num))) + k
        return [int(i) for i in str(x)]

mesin_hitung = Solution()
print(mesin_hitung.addToArrayForm([1, 2, 0, 0], 34))
