class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def message(self):
        print(f"{self.year} {self.make} {self.model} engine started!")

x = Car("Toyota", "Corolla", "2020")
x.message()
    