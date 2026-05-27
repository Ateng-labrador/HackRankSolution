import cmath

def converImaginary(z):
    """
    z = complex
    """
    r = cmath.sqrt((z.imag)**2 + (z.real)**2)
    pha = cmath.phase(z)
    return abs(r), pha

if __name__ == "__main__":
    s = complex(input())
    x, y = converImaginary(s)
    print(x)
    print(y)
