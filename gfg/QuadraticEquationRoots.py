import math

def quadraticEquationRoots(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = math.floor((-b + math.sqrt(D)) / (2.0 * a))
        x2 = math.floor((-b - math.sqrt(D)) / (2.0 * a))
        res = [x1, x2]
        return res
    elif D == 0:
        x1 = math.floor((-b + math.sqrt(D)) / (2.0 * a))
        return [x1, x1]
    elif D < 0:
        return "Imaginary"
    else:
        return "Error"

print(quadraticEquationRoots(3, 3, 18))
