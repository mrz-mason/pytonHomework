res_list = []
res = 0
while True:
    mus = input("Введите три любимых жанра музыки:")
    res_list.append(mus)
    res = res + 1
    if res == 3:
        break
print("Ваши предпочтения:", res_list)