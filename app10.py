# Тренировка по атрибутам классов

class MyClass:
    def my_method(self):
        print("Здравствуйте")

class Humans:
    def __init__(self, name="Sara", age=33, age_of_child=25):
        self.name = name
        self.age = age
        self.age_of_child = age_of_child
        self.caramba()
        mike = Ben()
        self.rondo = 78


    def sum_of_all_age(self):
        print(self.age + self.age_of_child)
        self.proba = 232
        pass

    def sum_of_all_age2(self):
        self.sum_of_all_age()
        print(self.age + self.age_of_child +2)
        pass

    def caramba (self):
        print("caramba")

class Ben:
    def __init__(self):
        pass
        print("supercBen")

    def test(self):
        a=5
        b=7
        c = a+b
        print(c)

    def testprint(self):
        c = 13
        print(c)

# Правильное применение:
bob_the_object = MyClass()  # Познакомьтесь, это Боб – экземпляр класса.
bob_the_object.my_method()  # Бобу поручено поприветствовать вас!

man = Humans("John", 25, 40)
man.sum_of_all_age()
man.sum_of_all_age2()

woman = Humans()
woman.sum_of_all_age()
woman.sum_of_all_age2()

john = Ben()
john.test()
john.testprint()



print(dir(bob_the_object))
print(dir(man))
print(dir(john))

print(dir(woman))