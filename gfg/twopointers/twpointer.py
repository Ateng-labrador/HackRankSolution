class Algoritma:
    @staticmethod
    def twopointer_naive(arr, x):
        """
        Naive Method - O(n^2) Time and O(1) Space
        """
        for i in range(len(arr)):
            # For each element arr[i], check every
            # other element arr[j] that comes after it
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == x:
                    return True
        return False

    @staticmethod
    def TwoPointer(arr, x):
        L = 0
        R = len(arr) - 1
        while L < R:
            m = arr[L] + arr[R]
            if m > x:
                R -= 1
            elif m < x:
                L += 1
            else:
                return True
        return False
        
                
arr = [-3, -1, 0, 1, 2]
target = -2
print(Algoritma.TwoPointer(arr, target))
