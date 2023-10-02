num = int(input("Введите число:"))
res = 0
res2 = 1
if num > 0:
    dig = num % 10
    res = res + dig
    res2 = res2 * dig
    num = num // 10
if dig // 2 == 0 and res // 3 == 0:
    print("Ваше число делится на 6")
else:
    print("Ваше число не делится на 6")
#pass