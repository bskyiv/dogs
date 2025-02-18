# Тренировка по атрибутам классов

class Humans:
    def __init__(self, name, age, age_of_child):
        self.name = name
        self.age = age
        self.age_of_child = age_of_child

    def sum_of_all_age(self):
        print(self.age + self.age_of_child)

    def sum_of_all_age2(self):
        self.sum_of_all_age()
        print(self.age + self.age_of_child +2)

man = Humans("John", 25, 40)
man.sum_of_all_age()
man.sum_of_all_age2()




