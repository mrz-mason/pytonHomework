print("Подождите идёт загрузка . . .")
from Project_Fitness_code import fitness

print("Приветсвую вас в клубе GYM.BONG.Наш слоган: Мы курим и качаемся, качаемся и курим.", end = '')
while (text := input("Что вас интересует?: ")) != 'это всё':
    fitness(text)
    print("Если не осталось больше никаких вопросов скажите, пожалуйста: это всё \n")