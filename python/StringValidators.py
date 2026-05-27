def isalnum1(s):
    res = False
    for x in s:
        if x.isalnum():
            res = True
            break
    return res


def isalpha1(s):
    res = False
    for x in s:
        if x.isalpha():
            res = True
            break
    return res

def isalnum1(s):
    res = False
    for x in s:
        if x.isalnum():
            res = True
            break
    return res

def isdigit1(s):
    res = False
    for x in s:
        if x.isdigit():
            res = True
            break
    return res

def islower1(s):
    res = False
    for x in s:
        if x.islower():
            res = True
            break
    return res

def isupper1(s):
    res = False
    for x in s:
        if x.isupper():
            res = True
            break
    return res


if __name__ == "__main__":
    # ini membaca seluruh string sekaligus
    x = input()
    print(isalnum1(x))
    print(isalpha1(x))
    print(isdigit1(x))
    print(islower1(x))
    print(isupper1(x))