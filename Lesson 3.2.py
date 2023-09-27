category = input("Категория тоавров: ")
wish = input("Предпочтения: ")
if category == "Молочные продукты" and wish == "Фермерское":
    print("Экоферма")
if category == "Молочные продукты" and wish != "Фермерское":
    print("Моё село")
if category == "Хлеб" and wish != "Цельнозерновой":
    print("Пекарня дяди Олега")
if category == "Хлеб" and wish != "Цеольнозерновой":
    print("Хлебозавод Сириус")
