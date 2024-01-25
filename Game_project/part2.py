import random
import time
from colorama import init, Fore, Back, Style

def main():
    hero_health = 100
    monster_health = 50

    while hero_health > 0 and monster_health > 0:
        monster_damage = random.randint(5, 15)
        monster_armor = random.randint(30,40)

        hero_damage = random.randint(10, 20)
        hero_armor = random.randint(30, 40)

        monster_health -= hero_damage
        hero_health -= monster_damage

        hero_armor -= monster_damage
        monster_armor -= hero_damage

        print(Fore.RED + "\nМонстр нанес", monster_damage, "урона")
        print(Fore.GREEN + "Вы нанесли", hero_damage, "урона")

        print(Fore.RED + "Монстр не нанёс урона, но понизил вашу защиту на ", monster_damage, "")
        print(Fore.GREEN +"Вы не нанесли урона по монстру, а попали по броне и снизили его защиту на", hero_damage, "")

        print(Fore.RED + "Остаток здоровья монстра:", monster_health)
        print(Fore.GREEN + "Остаток вашего здоровье:", hero_health)
        print("")
        time.sleep(3)

    if hero_health <= 0:
        print(Fore.RED + "Вы проиграл бой!")
    else:
        print(Fore.GREEN + "Вы победил монстра!")
    print(Style.RESET_ALL)
if __name__ == "__main__":
    main()