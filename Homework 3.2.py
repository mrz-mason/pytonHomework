game = input("Введите game для начала:")
if game == "game":
    print("Начало игры")
repeat = 0
while repeat != 3:
    res = int(input("Введите число:"))
    repeat = repeat + 1
    if res == 5:
        print("Вы угадали")
    elif repeat == 3:
        print("Вы проиграли")