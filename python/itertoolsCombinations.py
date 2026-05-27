from itertools import combinations

# up to size k

def combinator(r, i):
    for j in range(1, int(i) + 1):
        for k in combinations(sorted(r.upper()), j):
            print("".join(k))


if __name__ == "__main__":
    r, i = input().split()
    x = combinator(r, i)
    
