import random

class Character:
    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack(self, opponent):
        damage = self.strength - opponent.defense
        if damage > 0:
            print(f"{self.name} атакует {opponent.name} и наносит {damage} урона!")
            opponent.health -= damage
        else:
            print(f"{self.name} атака не оказывает никакого влияния на {opponent.name}. Потому что прошла по броне ")

    def is_alive(self):
        return self.health > 0


def calculate_damage_with_armor(damage, armor, armor_reduction_chance):
    if random.random() < armor_reduction_chance:
        reduced_damage = damage - armor
        if reduced_damage > 0:
            return reduced_damage
    return damage


hero = Character("Герой", 10, 5, 100)
monster = Character("Монстр", 8, 3, 80)

while hero.is_alive() and monster.is_alive():
    hero.attack(monster)
    if monster.is_alive():
        monster.attack(hero)

if hero.is_alive():
    print("Победа за вами!")
else:
    print("Вы проиграли")