from itertools import permutations

s, i = input().split()
for i in list(permutations(sorted(s.upper()), int(i))):
    print("".join(i))
