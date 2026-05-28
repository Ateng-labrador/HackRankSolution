import numpy as np

N = np.array(input().split(), dtype=float)
x = int(input())
print(np.polyval(N, x))
