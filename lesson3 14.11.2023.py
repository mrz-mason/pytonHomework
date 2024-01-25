#Запрограммируй класс Rectangle (прямоугольник):
# 1) Создай конструктор класса. Он должен создавать прямоугольник со свойствами: длина и ширина (вводятся с клавиатуры).
# 2) Создай метод, печатающий информацию о фигуре. Он должен выводить данные: «Дан прямоугольник с длиной _ и шириной _».
# 3) Создай метод, вычисляющий и возвращающий периметр прямоугольника. 4) Создай метод, вычисляющий и возвращающий площадь прямоугольника.

class Rectangle:
    def __init__(self):
        self.length = float(input("Введите длину прямоугольника: "))
        self.wide = float(input("Введите ширину прямоугольника: "))

    def print_info(self):
        print("Дан прямоугольник с длинной", self.length, "и шириной", self.wide)

    def get_perimetr(self):
        return (self.length + self.wide)*2
    def get_area(self):
        return self.length * self.wide

rectangle = Rectangle()
print("Периметр прямоугольника: ", rectangle.print_info())
print("Площадь прямоугольника: ", rectangle.get_area())
