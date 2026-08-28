class Solution:
    def fourSum(self, arr, x):
        n = len(arr)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                L = j + 1
                R = n - 1
                while L < R:
                    total = arr[i] + arr[j] + arr[L] + arr[R]
                    if  total < x:
                        L += 1
                    elif total > x:
                        R -= 1
                    else:
                        return True
        return False

                        

mesin_hitung = Solution()
arr1 = [1, 5, 1, 0, 6, 0]
x1 = 7
arr2 = [1, 2, 3, 4, 5]
x2 = 50
print(mesin_hitung.fourSum(arr1, x1))
print(mesin_hitung.fourSum(arr2, x2))
