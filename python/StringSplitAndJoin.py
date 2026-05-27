def split_and_join(line):
    test1 = line.split(" ")
    test2= '-'.join(test1)
    return test2

if __name__ == "__main__":
    N = str(input())
    x = split_and_join(N)
    print(x)

