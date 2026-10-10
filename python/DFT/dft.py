import cmath

def widdle(N):
    res = []
    for m in range(N):
        row = []
        for n in range(N):
            W = cmath.exp(1j*2*cmath.pi * m * n / N)
            row.append(W)
        res.append(row)
    return res
     
def dft(x):
    widdle_matrix = widdle(len(x))
    res = [0] * len(x)
    for m in range(len(x)):
        for n in range(len(widdle_matrix[0])):
            res[n] += widdle_matrix[m][n] * x[n]
    return (2 / len(x)) * res

def dft1(x):
    N = len(x)
    res = []
    
    for k in range(N):
        sum_val = 0
        for n in range(N):
            # Menghitung twiddle factor langsung di dalam loop
            W = cmath.exp(-1j * 2 * cmath.pi * k * n / N)
            sum_val += x[n] * W
        res.append(sum_val)
    return res
 

# manual

X = [2, 1, 4, 7, 6, 3, 1, 9]
print(dft1(X))
