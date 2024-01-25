#Запрограммируй класс Student:
# 1) Создай конструктор класса. Он должен создавать студента со свойствами: имя, средний балл (передаются в конструктор) и посещаемый курс по выбору (по умолчанию «-»).
# 2) Создай метод, печатающий информацию о студенте. Он должен выводить данные в формате имя:ХХХ, средний бал:XXX и т.д
# 3) Создай метод, устанавливающий курс по выбору. Название курса должно запрашиваться с клавиатуры и сохраняться как свойство объекта.

class Student:
    def __init__(self, name, average_score, optional_course):
        self.name = name
        self.average_score = average_score
        self.optional_course = optional_course

    def print_info(self):
        print("Имя: ", self.name,)
        print("Средний балл ученика/студента: ",self.average_score)
        print("Какой курс посещает: ",self.optional_course)

    def set_optional_course(self):
        self.optional_course = input("Введите название курса по выбору: ", )

student1 = Student("Бабчёнок Олег Юрьевич",2, 3)
student1.print_info()
student1.set_optional_course()
student1.print_info()

