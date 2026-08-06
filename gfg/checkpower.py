import math

def checkforpower(x, y):
    T = "true"
    F = "false"
    try:
        x = math.log(y, x)
        return T
    except ZeroDivisionError:
        return F
    except ValueError:
        return F
    

print(checkforpower(1, 4))