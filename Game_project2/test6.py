def repeat_code():
    def chosen_option():
        # Представленные варианты
        options = [
            "Дом одной из жертв",
            "Офис",
            "Переулок"
        ]

        # Выводим варианты на экран
        print("Выберите один из предложенных вариантов:")
        for i, option in enumerate(options):
            print(i + 1, "-", option)

        # Запрашиваем ответ у пользователя
        chosen_option = input("Введите номер выбранного варианта: ")

        # Проверяем, что введенный номер корректен
        if not chosen_option.isdigit() or int(chosen_option) < 1 or int(chosen_option) > len(options):
            print("Некорректный номер варианта!")
            return

        # Запоминаем выбранный вариант
        chosen_option = options[int(chosen_option) - 1]

        # Строим диалог на основе выбранного варианта
        print("Вы выбрали:", chosen_option)
        print("...")
        if chosen_option == "Дом одной из жертв":
            print("Вы подъезжаете к дому жертвы и видете напротив этого дома, дом соседа, который сидит на крыльце")
            print("Вы заходите в дом")
            def proof1():
                proof1 = input("Что вы хотите сделать? (поиск улик на первом этаже/поиск улик на втором этаже): ")
                if proof1 == "поиск улик на первом этаже":
                    print("Вы обошли весь этаж найдя следы крови, которые не были обнаруженны при первичном осмотре места приступления.")
                    print("Вы взяли её на анализ")
                    print("Также детально осмотрев место борьбы жертвы и приступника. Вы анализируя как пристпник мог уйти и идёте по тому пути. \nВыйдя на этот путь недалеко от дома вы находите орудие преступления")
                    step = input("Что делать дальше ? (пойти поговорить с соседом/поехать в полицейский участок)")
                    if step == "пойти поговорить с соседом":
                        print("Выйдя из дома вы напривлись к дому соседа")
                        print("Здраствуйте, сэр, Я детекив ... , могу я задать вам несколко вопросов ?")
                        print("Добрый вечер, детектив. Да, конечно, слушаю")
                        print("Как вы охарактеризуете жертву недавних событий, то есть вашего соседа ?")
                        print("Рассказывает о соседе")
                        step1 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")
                        if step1 == "записать в блакнот":
                            print("Вы записали всё о чём рассказал вам глава отдела")
                        elif step1 == "слушать дальше":
                            print("Вы решили продолжить слушать дальше")
                        print("Хм, а не подскажите, может быть у него были с кем-нибудь конфликты ?")
                        print("Нет, абсолютно нет")
                        step2 = input("   показать фотографию / спросить о его семье   ")
                        if step2 == "показать фотографию":
                            print("Вы показали фотографию")
                            print("О, да. Узнаю одного двух людей с фото. Первый мой сосед. А воторой это начальник полиции")
                            print("Спасибо за информацию")
                            print("После разговора вы уехали в полицейский участок")
                        elif step2 == "спросить о его семье":
                            print("Нет у него семьи. Родителей уже давно нет... \nА вот жена ушла от него и сын когда вырос и стал самостоятельным совсем забыл о своём старике")
                            print("Вы записали это в блакнот")
                            print("Спасибо за информацию")
                        print("Закончив разговор вы уехали в полицейский участок")
                    elif step == "поехать в полицейский участок":
                        print("Вы уехали в полицеский участок")
                elif proof1 == "поиск улик на втором этаже":
                    print("Вы заходите в дом и сразу направляетесь на второй этаж. В надежде что там есть какие-либо зацепки")
                    print("Поднявшись на второй этаж вы видете 3 комнаты")
                    step3 = input("В какую комнату зайдём в первую очередь? (слева/справа/прямо)")
                    if step3 == "слева":
                        print("Зайдя в комнату слева вы увидели кабинет. В которм уже давно никого не было.")
                        print("Всё было в прильнчом слое пыли, в углах даже паутина появилась. ")
                        print("Вы осмотрели книжные полки и стол. Но кроме очень страх документов и книг вы ничего не нашли")
                        print("Потом вы пошли в комнату напротив этой. Там была детская в которой тоже уже давно никто не бывал.")
                        print("Поискав там, вы тоже ничего не нашли")
                        print("Потом вы пошли в оставшуюся комнату. Но увы, это была супружеская спальня. В котрой точно также никого не было уже давно")
                        print("Вы обыскали и эту комнату, но как и в других комнатах ничего не нашли")
                        print("Поняв, что второй этаж заброшен и им никто не пользуется. Вы спустились на первым и решили поискать там.")
                        print("Вы обошли весь этаж найдя следы крови, которые не были обнаруженны при первичном осмотре места приступления.")
                        print("Вы взяли её на анализ")
                        print("Также детально осмотрев место борьбы жертвы и приступника. Вы анализируя как пристпник мог уйти и идёте по тому пути. \nВыйдя на этот путь недалеко от дома вы находите орудие преступления")
                        step4 = input("Что делать дальше ? (пойти поговорить с соседом/поехать в полицейский участок)")
                        if step4 == "пойти поговорить с соседом":
                            print("Выйдя из дома вы напривлись к дому соседа")
                            print("Здраствуйте, сэр, Я детекив ... , могу я задать вам несколко вопросов ?")
                            print("Добрый вечер, детектив. Да, конечно, слушаю")
                            print("Как вы охарактеризуете жертву недавних событий, то есть вашего соседа ?")
                            print("Рассказывает о соседе")
                            step5 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")
                            if step5 == "записать в блакнот":
                                print("Вы записали всё о чём рассказал вам глава отдела")
                            elif step5 == "слушать дальше":
                                print("Вы решили продолжить слушать дальше")
                            print("Хм, а не подскажите, может быть у него были с кем-нибудь конфликты ?")
                            print("Нет, абсолютно нет")
                            step6 = input("   показать фотографию / спросить о его семье   ")
                            if step6 == "показать фотографию":
                                print("Вы показали фотографию")
                                print("О, да. Узнаю одного двух людей с фото. Первый мой сосед. А воторой это начальник полиции")
                                print("Спасибо за информацию")
                                print("После разговора вы уехали в полицейский участок")
                            elif step6 == "спросить о его семье":
                                print("Нет у него семьи. Родителей уже давно нет... \nА вот жена ушла от него и сын когда вырос и стал самостоятельным совсем забыл о своём старике")
                                print("Вы записали это в блакнот")
                                print("Спасибо за информацию")
                                print("Закончив разговор вы уехали в полицейский участок")
                        elif step4 == "поехать в полицейский участок":
                            print("Вы уехали в полицеский участок")
                    elif step3 == "справа":
                        print("Вы пошли в комнату справа. Там была детская в которой уже давно никто не бывал.")
                        print("Поискав там, вы ничего не нашли")
                        print("Зайдя в комнату напротив вы увидели кабинет. В которм уже тоже давно никого не было.")
                        print("Всё было в прильнчом слое пыли, в углах даже паутина появилась. ")
                        print("Вы осмотрели книжные полки и стол. Но кроме очень старых документов и книг вы ничего не нашли")
                        print("Потом вы пошли в оставшуюся комнату. Но увы, это была супружеская спальня. В котрой точно также никого не было уже давно")
                        print("Вы обыскали и эту комнату, но как и в других комнатах ничего не нашли")
                        print("Поняв, что второй этаж заброшен и им никто не пользуется. Вы спустились на первым и решили поискать там.")
                        step7 = input("Что делать дальше ? (пойти поговорить с соседом/поехать в полицейский участок)")
                        if step7 == "пойти поговорить с соседом":
                            print("Выйдя из дома вы напривлись к дому соседа")
                            print("Здраствуйте, сэр, Я детекив ... , могу я задать вам несколко вопросов ?")
                            print("Добрый вечер, детектив. Да, конечно, слушаю")
                            print("Как вы охарактеризуете жертву недавних событий, то есть вашего соседа ?")
                            print("Рассказывает о соседе")
                            step8 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")
                            if step8 == "записать в блакнот":
                                print("Вы записали всё о чём рассказал вам глава отдела")
                            elif step8 == "слушать дальше":
                                print("Вы решили продолжить слушать дальше")
                            print("Хм, а не подскажите, может быть у него были с кем-нибудь конфликты ?")
                            print("Нет, абсолютно нет")
                            step9 = input("   показать фотографию / спросить о его семье   ")
                            if step9 == "показать фотографию":
                                print("Вы показали фотографию")
                                print("О, да. Узнаю одного двух людей с фото. Первый мой сосед. А воторой это начальник полиции")
                                print("Спасибо за информацию")
                                print("После разговора вы уехали в полицейский участок")
                            elif step9 == "спросить о его семье":
                                print("Нет у него семьи. Родителей уже давно нет... \nА вот жена ушла от него и сын когда вырос и стал самостоятельным совсем забыл о своём старике")
                                print("Вы записали это в блакнот")
                                print("Спасибо за информацию")
                                print("Закончив разговор вы уехали в полицейский участок")
                        elif step7 == "поехать в полицейский участок":
                            print("Вы уехали в полицеский участок")
                    elif step3 == "прямо":
                        print("Вы вы пошли в комнату которая была по прямой. Это была супружеская спальня. В котрой никого не было уже давно")
                        print("Вы обыскали и эту комнату, но ничего не нашли")
                        print("Зайдя в комнату слева вы увидели кабинет. В которм уже тоже давно никого не было.")
                        print("Всё было в прильнчом слое пыли, в углах даже паутина появилась. ")
                        print("Вы осмотрели книжные полки и стол. Но кроме очень старых документов и книг вы ничего не нашли")
                        print("Вы пошли в комнату справа. Там была детская в которой уже давно никто не бывал.")
                        print("Поискав там, вы ничего не нашли")
                        print("Поняв, что второй этаж заброшен и им никто не пользуется. Вы спустились на первым и решили поискать там.")
                        step10 = input("Что делать дальше ? (пойти поговорить с соседом/поехать в полицейский участок)")
                        if step10 == "пойти поговорить с соседом":
                            print("Выйдя из дома вы напривлись к дому соседа")
                            print("Здраствуйте, сэр, Я детекив ... , могу я задать вам несколко вопросов ?")
                            print("Добрый вечер, детектив. Да, конечно, слушаю")
                            print("Как вы охарактеризуете жертву недавних событий, то есть вашего соседа ?")
                            print("Рассказывает о соседе")
                            step11 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")
                            if step11 == "записать в блакнот":
                                print("Вы записали всё о чём рассказал вам глава отдела")
                            elif step11 == "слушать дальше":
                                print("Вы решили продолжить слушать дальше")
                            print("Хм, а не подскажите, может быть у него были с кем-нибудь конфликты ?")
                            print("Нет, абсолютно нет")
                            step12 = input("   показать фотографию / спросить о его семье   ")
                            if step12 == "показать фотографию":
                                print("Вы показали фотографию")
                                print("О, да. Узнаю одного двух людей с фото. Первый мой сосед. А воторой это начальник полиции")
                                print("Спасибо за информацию")
                                print("После разговора вы уехали в полицейский участок")
                            elif step12 == "спросить о его семье":
                                print("Нет у него семьи. Родителей уже давно нет... \nА вот жена ушла от него и сын когда вырос и стал самостоятельным совсем забыл о своём старике")
                                print("Вы записали это в блакнот")
                                print("Спасибо за информацию")
                                print("Закончив разговор вы уехали в полицейский участок")
                        elif step10 == "поехать в полицейский участок":
                            print("Вы уехали в полицеский участок")

                return

            proof1()

        elif chosen_option == "Офис":
            print("Офис, где работала жертва убийства, был словно погребен в мрачной атмосфере тайн и угроз.")
            print("Сразу пройдя на парков где и было совершено убийство. ")
            print("Я так и не смог ничего заметить, чтоб меня это привело хоть на немного к разгадке этой серии убиств")
            print("Тогда я решил подняться в офис в котором работала жертва")
            print("Весь офис пустовал, так как компания прекратила свою работу на время расследования.")
            print("Пройдя между множеством рабочих столов. Я дошёл до стола жертвы.")
            print("На столе было множество бумаг, как будто тут всё ещё кипит во всю работа")

            def proof():
                proof = input("Что вы хотите сделать? (поиск улик/поговорить с главой отедла): ")
                if proof == "поиск улик":
                    print("Вы обыскиваете рабочий стол жертвы. \n И находите в одном из ящиков старое фото вместе с новым, на котором изображены люди вместе с жертвой. \nНа новой фотографии было написано: Вот мы и снова встретились мои старые друзья")
                    step = input("Что вы хотите сделать? (поговорить с главой отдела/поехать в полицейский участок): ")

                    if step == "поговорить с главой отдела":
                        print("Вы начинаете беседу")
                        print("Вы подходите к главе отдела и спрашиваете: Могу ли я задать пару вопросов ?")
                        print("На что получаете положительный ответ")
                        print("Каким человеком была жертва?")
                        print("Рассказывает о жертве")
                        step1 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")

                        if step1 == "записать в блакнот":
                            print("Вы записали всё о чём рассказал вам глава отдела")
                        elif step1 == "слушать дальше":
                            print("Вы решили продолжить слушать дальше")

                        print(
                            "У меня есть ещё вопрос. Вы показываете фотографии. Кто на этих фото по-мимо самой жертвы ?")
                        print("На этом фото как вы видете есть я, также начальник полиции и наш старый друг который уже как пару месяцев не выходит на связь")
                        print("А где вы нашли это фото?")
                        print("В столе у жертвы")
                        print("Закончив разгвоор вы поехали в полицеский участок")

                    elif step == "поехать в полицейский участок":
                        print("Вы забрав все улики с собой, быстро ушли и поехали в полицеский участок")

                elif proof == "поговорить с главой отедла":
                    print("Вы подходите к главе отдела и спрашиваете: Могу ли я задать пару вопросов ?")
                    print("На что получаете положительный ответ")
                    print("Каким человеком была жертва?")
                    print("Рассказывает о жертве")
                    step2 = input(" Что будешь делать? (записать в блакнот/слушать дальше)")

                    if step2 == "записать в блакнот":
                        print("Вы записали всё о чём рассказал вам глава отдела")
                    elif step2 == "слушать дальше":
                        print("Вы решили продолжить слушать дальше")

                    print("У меня есть ещё вопрос. Вы показываете фотографии. Кто на этих фото по-мимо самой жертвы ?")
                    print("На этом фото как вы видете есть я, также начальник полиции и наш старый друг который уже как пару месяцев не выходит на связь")
                    print("А где вы нашли это фото?")
                    print("В столе у жертвы")
                    print("Закончив разгвоор вы поехали в полицеский участок")
                elif proof == "":
                    print("")
                return

            proof()

        elif chosen_option == "Переулок":
            print("В этом переулке вы сразу же находите улики. Это следы крови. А пройдя чуть дальше и орудие убийства.")
            print("Вы уехали в полицейский участок")
    chosen_option()

for i in range(3):

    def expertise():
        print("Приехав в полицейский участок где собраны все улики. Вы отдали их на экспертизу.")
        print("Выяснилось что кровь из офиса предлежит жертве и какому-то неизвестному человеку")
        print(
            "Так же кровь из дома предлежит жертве и тому же неизвестному человеку. Но на орудие убиства были отпечатки пальцев того самого соседа")
        print(
            "Но больше всего удивило, так это улики из переулка. Кровь что я нашёл совпадает с кровью жертвы, а также там были замечены и следы того же неизвестного мужчины.")
        print(
            "Бинго! На орудие убийства из подворотни были получены отпечатки пальцев неизвестного мужчины. Осталось пробить по базе и вызвать на допрос")
        print(
            "Вызвав по началу соседа той жертвы из дома. Мы проверили снова улики и совпадение было только с орудем убийства из дома.")
        print("Следовательно, его кто-то пытался подставить. Его мы отпустили.")
        print(
            "Мы нашли того самого человека с проишествия в переулке и вызвали на допрос. Он вёл себя подозрительно. Поэтому мы оставили его ещё на какое-то время")
        expertise = input("\n     продолжать давить на подозреваемого/сходить к начальнику полиции   ")
        if expertise == "продолжать давить на подозреваемого":
            print("В итоге путём допроса с отягощающими последствиями. Нам удалось выбить из него всю информацию")
            print(
                "Оказывается, что следующим бы был начальник полиции. Так как в школе вся эта компания, с фото, издевалась над ним. И он решил отомстить. Только на это понадобилось много лет\n")
            print("\n          ДЕЛО ЗАКРЫТО ")
        elif expertise == "сходить к начальнику полиции":
            print("Придя к начальнику полиции, я сообщил о хороших результатах. Чем сильно его обрадовал")
            print("Он решил сходить  и посмотреть что же это за зверь такой, что решил в его городе бесчинствовать.")
            print("Но только увидев его он узнал в нём того, самого мальчика над которым они издевались в школе")
            print("Подозреваемый увидев его тут же выдал всё. И о планах мести и о разработке плана и.т.д")
            print(
                "А также рассказал что, тот парень которого он убил в переулке был их жругом который уже давно не выходил на связь\n")
            print("\n          ДЕЛО ЗАКРЫТО ")

        return


    repeat_code()