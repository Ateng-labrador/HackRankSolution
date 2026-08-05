def factorial(n):
    res = 1
    while n > 1:
        res *= n
        if n != 1:
            n -= 1
        else:
            n = 1
    return res
        

print(factorial(4))