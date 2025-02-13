# Мои классы

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class ColorCat(Cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def info(self):
        print(f"I am a colorcat. My name is {self.name}.  I am {self.age} years old. My color is {self.color}.")

    def make_sound(self):
        print("Wow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")
