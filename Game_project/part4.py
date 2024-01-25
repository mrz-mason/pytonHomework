import time
from colorama import init, Fore, Back, Style

def choose_option1():
    # Представленные варианты
    options1 = [
        "Ты не представляешь, что со мной произошло",
        "Что случилось с замком?",
        "Как поживаешь старина?"
    ]

    # Выводим варианты на экран
    print("Выберите один из предложенных вариантов:")
    for i, option in enumerate(options1):
        print(i + 1, "-", option)

    # Запрашиваем ответ у пользователя
    chosen_option1 = input("Введите номер выбранного варианта: ")

    # Проверяем, что введенный номер корректен
    if not chosen_option1.isdigit() or int(chosen_option1) < 1 or int(chosen_option1) > len(options1):
        print("Некорректный номер варианта!")
        chosen_option1()

    # Запоминаем выбранный вариант
    chosen_option1 = options1[int(chosen_option1) - 1]

    # Строим диалог на основе выбранного варианта
    print("Вы выбрали:", chosen_option1)
    print("Продолжим ...")
    if chosen_option1 == "Ты не представляешь, что со мной произошло":
        print(Fore.YELLOW + "Стражник удивлённо смотрит на вас и спрашивает: Что же такого могло произойти?")
        time.sleep(5)
        print(Fore.GREEN + "Вы рассказываете ему всё что с вами произошло во время отсутсвия")
        time.sleep(5)
        print(Fore.YELLOW + "Ух ты ж, мать моя, царстовей ей небесное, так вот кто спас нас всех от неменуемой гибели")
        print(Style.RESET_ALL)
        time.sleep(5)
        print("Стражник бежит к своему лорду доложить кто пришёл и что случилось")
        time.sleep(5)
        print("Вас спустя какое-то время отводят в замок к лорду")
        time.sleep(5)
        print("После того как вы ему повторно всё рассказали, в вашу честь устроили пир")
        time.sleep(5)
        print("После пира и вашего отдыха в этом городе, вы думаете, что делать дальше:")
        time.sleep(5)

        from part5 import chosen_option2
        chosen_option2()

    elif chosen_option1 == "Что случилось с городом?":
        print(Fore.YELLOW + "И тебе привет, ответил стражник")
        time.sleep(5)
        print(Fore.YELLOW + "Да вот как-то всё неожиданно произошло, только вчера всё было как во тьме")
        time.sleep(5)
        print(Fore.YELLOW + "А сегодня солнышко светит, птички поют, красота одним словом.")
        time.sleep(5)
        print(Fore.GREEN + "Странно ответили вы.")
        time.sleep(5)
        print(Fore.YELLOW + "Не поспоришь. Я вот думаю, что это всё наша богиня, которой мы молились столько лет, всё-таки снизошла на нас и избавила от этого проклятья")
        time.sleep(5)
        print(Fore.YELLOW + "Хотя, если честно, то не один я так думаю, а весь город так считает, да и лорд вроде как не против этих слухов")
        print(Style.RESET_ALL)
        time.sleep(5)
        print("Вы не став рассказывать что на самом деле произошло, прошли в город, передохнули некоторое время, особенно это важно после таких событий")
        time.sleep(5)
        print("Теперь перед вами стоит выбор, что делать дальше: ")
        time.sleep(5)

        from part5 import chosen_option2
        chosen_option2()

    elif chosen_option1 == "Как поживаешь старина?":
        print(Fore.YELLOW + "Какой я тебе страина!?")
        print(Style.RESET_ALL)
        time.sleep(5)
        print("Вы понимаете что всё-таки этот город не будет вам так радушен, как вы ожидали, уходите прочь")
        time.sleep(5)
        print("Теперь перед вами стоит выбор, что делать дальше: ")
        time.sleep(5)

        from part6 import choose_option3
        choose_option3()


choose_option1()
