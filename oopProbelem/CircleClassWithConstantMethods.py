import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_volume(self):
        return 4/3 * math.pi * self.radius**3

    def get_volume_surface(self, t):
        return math.pi * self.radius**2 * t

x = Circle(5)
print(x.get_area())
print(x.get_volume())
print(x.get_volume_surface(5))
