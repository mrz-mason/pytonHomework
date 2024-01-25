from random import randint, choice
def plate ():
    letter = 'АВЕКМНОРСТУХ'
    license = choice(letter) + str (randint(100,999)) + choice(letter) + choice(letter) + str(randint(10,99))
    return license
print(plate)

