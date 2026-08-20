class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def dimensi(self):
        return f"{self.length} x {self.width}"

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

x = Rectangle(10, 5)
print(x.dimensi)
print(x.calculate_area())
print(x.calculate_perimeter())
