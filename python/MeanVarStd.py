import numpy as np


a = np.array([[1, 2], [3, 4]])
a_new = a.flatten()

res_var = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        x = np.abs(a[i][j] - np.mean(a))**2
        res_var += x

var = res_var / (a.size)


res_std = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        x = np.sqrt(np.abs(a[i][j] - np.mean(a))**2)
        res_std += x
std = res_std / (a.size)

res_var_1 = 0
for i in range(len(a_new)):
    x = np.abs(a_new[i] - np.mean(a_new))**2
    res_var_1 += x
var_new = res_var_1 / len(a_new)


res_std_1 = 0
for i in range(len(a_new)):
    x = np.sqrt(abs(a_new[i] - np.mean(a))**2)
    res_std_1 += x
std_new = res_std_1 / len(a_new)

print(var)
print(std)
print(var_new)
print(std_new)

        
