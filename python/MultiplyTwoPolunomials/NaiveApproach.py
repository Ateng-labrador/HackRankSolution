import cmath
import math


def multiply(A, B):
    """
    Approxtimation Navie Approach
    """

    m = len(A)
    n = len(B)

    # Initialize the product polynomial
    prod = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            prod[i + j] += A[i] * B[j]
    return prod


def widdle(N):
    res = []
    for k in range(N):
        row = []
        for n in range(N):
           W = cmath.exp(-1j*2*cmath.pi * k * n / N)
           row.append(W)
        res.append(row)
    return res
       

def dft(x):
    widle_matriks = widdle(len(x))
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(widle_matriks[0])):
            res[k] += widle_matriks[k][n] * x[n]
    return res


def dct1(x):
    res = [0] * len(x)
    for k in range(len(x)):
        for n in range(len(x)):
            if n == 0 or n == len(x) - 1:
                alpha = 1/2
            else:
                alpha = 1
            res[k] += 2 *  alpha * x[n] * math.cos(cmath.pi * k * n / (len(x) - 1))
    return res


def dct2(x):
    res = [0] * len(x)

    for k in range(len(x)):
        for n in range(len(x)):
            res[k] += 2 * x[n] * math.cos(cmath.pi * k * (2*n+1) / (2 * len(x)))
    return res


def multiplyAlgorithm(A, B):
    pass


def fft(x):
    N = len(x)
    if N == 1:
        return x
    odd_res = fft(x[1::2])
    even_res = fft(x[::2])
    res = [0] * N
    for k in range(N//2):
        W = cmath.exp(-1j * 2 * cmath.pi  * k / N)
        res[k] = even_res[k] * W*odd_res[k]
        res[k + N//2] = even_res[k] - W*odd_res[k]
    return res
