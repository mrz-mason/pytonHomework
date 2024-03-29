"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

while True:
    name = input("Введите имя студента: ")
    if name == "стоп":
        break
num_subjects = int(input("Введите число предметов: "))
total_score = 0
for i in range(num_subjects):
    score = int(input(f"Введите число баллов по предмету {i+1}: "))
    total_score += score

print(f"Итоговый счёт: {total_score}")

if total_score > 80:
    print("Наградить дипломом.")
elif total_score > 50 and total_score <= 80:
    print("Наградить похвальной грамотой.")
else:
    print("Выдать грамоту об участии.")