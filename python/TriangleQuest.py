def TriangleQuest(N):
    for i in range(1, N):
        print(int((i * (pow(10, i) - 1)) // 9)) 


s = int(input())
TriangleQuest(s)
