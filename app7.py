class MyClass:
    def first_method(self):
        return "Привет от первого метода!"

    def second_method(self):
        message = self.first_method()
        print(message)  # Выведет: "Привет от первого метода!"

obj = MyClass()
obj.second_method()  # Выведет: "Привет от первого метода!"