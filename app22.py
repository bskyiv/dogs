#

class Parents():
    def __init__(self, mom, dad):
        self.mom = "mom1"
        self.dad = "dad1"

class Doughter(Parents):
    def __init__(self, doughter):
#       super().__init__("Olia", "Joe")
        super().__init__("Olia", "Joe")
        self.doughter = doughter


parentsOfChild = Parents("Xu", "Mike")
print(parentsOfChild.mom, parentsOfChild.dad)

first = Doughter("Ann")
print (first.mom, first.dad)

print (first.doughter)


