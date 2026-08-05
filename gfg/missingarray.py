def missingarray(a):
    for i in range(1, len(a) + 2):
        fnd = False
        for j in range(len(a)):
            if a[j] == i:
                print(f"nilai arr : {a[j]} pada indeks {j}")
                print(f"nilai pemanding : {i}")
                fnd = True
                break
        if fnd == False:
            print(f"nilai yang kurang : {i}")


def missingNum(arr):
    n = len(arr) + 1
    sumarr = (n*(n + 1))//2
    sumarrtrue = sum(arr)
    return sumarr - sumarrtrue
        


if __name__ == "__main__":
    A = [1, 2, 3, 5]
    print(missingarray(A))
