import sys

sys.set_int_max_str_digits(10000)

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        x = int("".join(map(str, num))) + k
        return [int(i) for i in str(x)]