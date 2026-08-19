class BubbleSort:
    @staticmethod
    def bubbleSort(A):
        n = len(A)
        while n > 1:
            newn = 0
            for i in range(1, n):
                if A[i - 1] > A[i]:
                    (A[i - 1], A[i]) = (A[i], A[i - 1])
                    newn = i
            n = newn
        return A

    @staticmethod
    def bubbleSortOptimiz(A):
        n = len(A)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if A[i - 1] > A[i]:
                    (A[i - 1], A[i]) = (A[i], A[i - 1])
                    swapped = True
            n -= 1
        return A

    @staticmethod
    def bubbleSortSwap(A):
        n = len(A)
        while n > 1:
            newn = 0
            for i in range(1, n):
                if A[i - 1] > A[i]:
                    (A[i - 1], A[i]) = (A[i], A[i - 1])
                    newn = i
            n = newn
        return A

x = [2, 2, 6, 1, 7]
y1 = BubbleSort.bubbleSort(x)
y2= BubbleSort.bubbleSortOptimiz(x)
y3 = BubbleSort.bubbleSortSwap(x)
print(y1)
print(y2)
print(y3)
