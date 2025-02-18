import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def method3(self):
        return "Привет от 3 метода!"

    def method4(self):
         message = self.first_method()
         print(message)  # Выведет: "Привет от 3 метода!"


class MyClass:
    def first_method(self):
        return "Привет от первого метода!"

    def second_method(self):
        message = self.first_method()
        print(message)  # Выведет: "Привет от первого метода!"

obj = MyClass()
obj.second_method()  # Выведет: "Привет от первого метода!"

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()