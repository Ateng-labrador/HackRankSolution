def fibonanci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonanci(n - 1) + fibonanci(n - 2)


if __name__ == "__main__":
    print(fibonanci(10))

    