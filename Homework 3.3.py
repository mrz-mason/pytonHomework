log = input("Введите логин:")
for i in log:
    if i == "=?*^$№@_":
        break
print("Вы использовали запрещенные символы: =?*^$№@_ ")
for i in log:
    if i != "=?*^$№@_ ":
        break
print("Логин одобрен")