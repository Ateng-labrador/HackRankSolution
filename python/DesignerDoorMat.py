# Unsolved

import math

def DoorMar(N, M):
    if N % 2 != 0 and M != 3*N:
        print("Error Input")
    else:
        for i in range(M):
            for j in range(N):
                print("-")

if __name__ == "__main__":    
    N = int(input())
    M = int(input())
    x = DoorMar(N, M)
    print(x)