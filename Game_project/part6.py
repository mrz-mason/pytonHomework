import time
from colorama import init, Fore, Back, Style


def choose_option3():
    # Представленные варианты
    options3 = [
        "Вы передумали и ушли в другой город",
        "Вы ушли в лес",
        "Вы передумали и ушли иследовать регион"
    ]

    # Выводим варианты на экран
    print("Выберите один из предложенных вариантов:")
    for i, option in enumerate(options3):
        print(i + 1, "-", option)

    # Запрашиваем ответ у пользователя
    chosen_option3 = input("Введите номер выбранного варианта: ")

    # Проверяем, что введенный номер корректен
    if not chosen_option3.isdigit() or int(chosen_option3) < 1 or int(chosen_option3) > len(options3):
        print("Некорректный номер варианта!")
        return

    # Запоминаем выбранный вариант
    chosen_option3 = options3[int(chosen_option3) - 1]

    # Строим диалог на основе выбранного варианта
    print("Вы выбрали:", chosen_option3)
    print("Продолжим ...")
    if chosen_option3 == "Вы передумали и ушли в другой город":
        print(Fore.MAGENTA + "Вас окинула обида на этот город, поэтоу вы не стали ничего рассказывать стражнику")
        time.sleep(5)
        print("Вы успешно, а может и не очень, ушли в другой город")
        time.sleep(5)
        print("Посмотрим что вас там ожидает")
        print(Style.RESET_ALL)
        time.sleep(5)
    elif chosen_option3 == "Вы ушли в лес":
        print(Fore.MAGENTA + "Вы как и планировали ушли в лес")
        time.sleep(5)
        print("Посмотрим что вас там ожидает")
        print(Style.RESET_ALL)
        time.sleep(5)
    elif chosen_option3 == "Вы передумали и ушли иследовать регион":
        print(Fore.MAGENTA + "Вы встали на ровном месте, перед лесом и решили не идти туда")
        time.sleep(5)
        print("Зачем идти туда, не знаю куда. Поэтому открыв карту вы напрвились иследовать регион")
        time.sleep(5)
        print("Посмотрим что вас там ожидает")
        print(Style.RESET_ALL)
        time.sleep(5)


choose_option3()