class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model
#   def __str__(self):
#       return "Car: {} {}".format(self.make, self.model)
    def typeOfCar(self):
         print("This is a {} {}".format(self.make, self.model))


a = Car("Ford", "Mustang")
a.typeOfCar()

class Usedcar(Car):
#   def __init__(self, make, model):
    def __init__(self, parent=None, model=None, make=None):
        super().__init__(parent)
    def allTypeOfCar(self):
        print("This is a {} {} {}".format(self.make, self.model))

b = Usedcar("Honda", "Mustang")
b.allTypeOfCar()
