class Solution:
    def findTheDistanceValue(self, arr1 , arr2, d):
        res = 0
        for i in range(len(arr1)):
            check = True
            for j in range(len(arr2)):
                x = abs(arr1[i] - arr2[j])
                if x <= d:
                    check = False
            if check:
                res += 1
        return res

mesin_hitung = Solution()
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]

arr12 = [1,4,2,3]
arr13 = [-4,-3,6,10,20,30]

arr121 = [2,1,100,3]
arr131 = [-5,-2,10,-3,7]

print(mesin_hitung.findTheDistanceValue(arr1, arr2, 2))
print(mesin_hitung.findTheDistanceValue(arr12, arr13, 3))
print(mesin_hitung.findTheDistanceValue(arr121, arr131, 6))
