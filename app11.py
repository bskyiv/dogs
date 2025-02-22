class Clone:
    def __init__(self, name):
        self.name = name
    def addValToSelf(self):
        self.val = 55

    def make_new_clone(self, name):
        return Clone(name)

sheep_1 = Clone('Dolly')
sheep_2 = sheep_1.make_new_clone('Sally')
sheep_3 = sheep_2.make_new_clone('Bobby')
sheep_1.addValToSelf()

print (sheep_1.name) # 'Dolly'
print(sheep_1.val)

print (sheep_2.name) # 'Sally'
#print(sheep_2.val)

print (sheep_3.name) # 'Bobby'
#print(sheep_3.val)


print (dir(sheep_1))
print (dir(sheep_2))
print (dir(sheep_3))
