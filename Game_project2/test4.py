def expertise():
    print("Приехав в полицейский участок где собраны все улики. Вы отдали их на экспертизу.")
    print("Выяснилось что кровь из офиса предлежит жертве и какому-то неизвестному человеку")
    print("Так же кровь из дома предлежит жертве и тому же неизвестному человеку. Но на орудие убиства были отпечатки пальцев того самого соседа")
    print("Но больше всего удивило, так это улики из переулка. Кровь что я нашёл совпадает с кровью жертвы, а также там были замечены и следы того же неизвестного мужчины.")
    print("Бинго! На орудие убийства из подворотни были получены отпечатки пальцев неизвестного мужчины. Осталось пробить по базе и вызвать на допрос")
    print("Вызвав по началу соседа той жертвы из дома. Мы проверили снова улики и совпадение было только с орудем убийства из дома.")
    print("Следовательно, его кто-то пытался подставить. Его мы отпустили.")
    print("Мы нашли того самого человека с проишествия в переулке и вызвали на допрос. Он вёл себя подозрительно. Поэтому мы оставили его ещё на какое-то время")
    expertise = input("\n     продолжать давить на подозреваемого/сходить к начальнику полиции   ")
    if expertise == "продолжать давить на подозреваемого":
        print("В итоге путём допроса с отягощающими последствиями. Нам удалось выбить из него всю информацию")
        print("Оказывается, что следующим бы был начальник полиции. Так как в школе вся эта компания, с фото, издевалась над ним. И он решил отомстить. Только на это понадобилось много лет\n")
        print("\n          ДЕЛО ЗАКРЫТО ")
    elif expertise == "сходить к начальнику полиции":
        print("Придя к начальнику полиции, я сообщил о хороших результатах. Чем сильно его обрадовал")
        print("Он решил сходить  и посмотреть что же это за зверь такой, что решил в его городе бесчинствовать.")
        print("Но только увидев его он узнал в нём того, самого мальчика над которым они издевались в школе")
        print("Подозреваемый увидев его тут же выдал всё. И о планах мести и о разработке плана и.т.д")
        print("А также рассказал что, тот парень которого он убил в переулке был их жругом который уже давно не выходил на связь\n")
        print("\n          ДЕЛО ЗАКРЫТО ")

    return

expertise()