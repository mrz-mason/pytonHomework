sum = int(input("Введите сумму: "))
sum2 = 0
hour = int(input("Введите текущий час: " ))
sale = 0
sale_persent = 0
if hour > 9 and hour < 13:
    sum2 = sum / 2
    sale = '50%'
    sale_persent = 0.5
elif hour > 19 and hour < 23:
    sum2 = sum / 4
    sale = '75%'
    sale_persent = 0.75
print("Стоимость общей покупки: ", sum, "\nСкидка составляет: ", sale, "\nИтого: ", sum * sale_persent)
