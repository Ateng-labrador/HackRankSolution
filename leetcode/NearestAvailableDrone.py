class Solution:
    """
    Salah
    """
    def nearestDrone(self, drones, target):
        res = 0
        for i in range(len(drones)-1):
            for j in range(len(drones[0])-1):
                res_x = abs(drones[i][j] - target[0])
                res_y = abs(drones[i][j+1] - target[1])
                if (res_x + res_y) <= drones[len(drones) - 1 - i]:
                    res += 1
        return res

mesin_hitung = Solution()
drones = [[0,0,8],[2,2,9]]
target = [3, 4]
print(mesin_hitung.nearestDrone(drones, target))

        