sum1 = 0
summa = []
while True:
    sum1 = float(input("Введите стоимость товара(Вводить до 0):"))
    summa.append(sum1)
    if sum1 == 0:
        break
print("Сумма без скидки:", sum(summa))
sale = int(input("Введите скидку:"))
print("Итого со скидкой:", sum(summa) / 100 * sale)