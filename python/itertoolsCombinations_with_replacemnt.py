from itertools import combinations_with_replacement


def combinator(r, i):
    for i in combinations_with_replacement(sorted(r.upper()), int(i)):
        print("".join(i))


if __name__ == "__main__":
    s, a = input().split()
    x = combinator(s, a)

