import time
from colorama import init, Fore, Back, Style

def choose_option2():
    # Представленные варианты
    options2 = [
        "Вы понимаете, что таких мест как это ещё множество, и что вас ещё жду новые приключения",
        "Решаете по-больше иследовать эту местность",
        "Попробуете останется ещё в этом городе и продолжите свой отдых"
    ]

    # Выводим варианты на экран
    print("Выберите один из предложенных вариантов:")
    for i, option in enumerate(options2):
        print(i + 1, "-", option)

    # Запрашиваем ответ у пользователя
    chosen_option2 = input("Введите номер выбранного варианта: ")

    # Проверяем, что введенный номер корректен
    if not chosen_option2.isdigit() or int(chosen_option2) < 1 or int(chosen_option2) > len(options2):
        print("Некорректный номер варианта!")
        return

    # Запоминаем выбранный вариант
    chosen_option2 = options2[int(chosen_option2) - 1]

    # Строим диалог на основе выбранного варианта
    print("Вы выбрали:", chosen_option2)
    print("Продолжим ...")
    if chosen_option2 == "Вы понимаете, что таких мест как это ещё множество, и что вас ещё жду новые приключения":
        print(Fore.MAGENTA +"Вы решаетесь всё-таки уйти из этого места и отрпавиться в приключения в другие регионы или страны")
        time.sleep(5)
        print("Вас ждут незабываемые приключения")
        print(Style.RESET_ALL)
        time.sleep(5)
    elif chosen_option2 == "Решаете по-больше иследовать эту местность":
        print(Fore.MAGENTA +"Вы решаетесь уйти из этого места, но вы думаете, что вам необходимо исследовать этот регион")
        time.sleep(5)
        print("Может тут есть намного больше тайн, чем кажется на первый взгляд")
        print(Style.RESET_ALL)
        time.sleep(5)
    elif chosen_option2 == "Попробуете останется ещё в этом городе и продолжите свой отдых":
        print(Fore.MAGENTA +"Вы приняли решение остаться")
        time.sleep(5)
        print("В итоге вы прожили там несколко лет и обзавелись семьей")
        print(Style.RESET_ALL)
        time.sleep(5)


choose_option2()
