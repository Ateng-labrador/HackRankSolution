def duplicate_arr(a):
    res = a
    for i in a:
        res.append(i)
    return res

if __name__ == "__main__":
    a = [1, 4, 1, 2]
    print(duplicate_arr(a))