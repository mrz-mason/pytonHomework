def is_magic_date(date):
    is_magic = date.split(".")
    return int(is_magic[0])*int(is_magic[1])==int(is_magic[2])%100
print(is_magic_date(input("Введите дату в формате дд.мм.гггг \n")))