# Тренировка по атрибутам классов

class MyClass:
    def my_method(self):
        print("Здравствуйте")

class Humans:
    def __init__(self, name, age, age_of_child):
        self.name = name
        self.age = age
        self.age_of_child = age_of_child
        self.caramba()
        a = Ben()

    def sum_of_all_age(self):
        print(self.age + self.age_of_child)

    def sum_of_all_age2(self):
        self.sum_of_all_age()
        print(self.age + self.age_of_child +2)

    def caramba (self):
        print("caramba")

class Ben:
    def __init__(self):
        pass
        print("supercBen")


# Правильное применение:
bob_the_object = MyClass()  # Познакомьтесь, это Боб – экземпляр класса.
bob_the_object.my_method()  # Бобу поручено поприветствовать вас!

man = Humans("John", 25, 40)
man.sum_of_all_age()
man.sum_of_all_age2()

print(dir(man))