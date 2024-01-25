import random

def coin():
    while True:
        x1 = random.randint(1, 2)
        x2 = random.randint(1, 2)
        x3 = random.randint(1, 2)
        for n in [x1, x2, x3]:
            if n == 1:
                print("Орёл ", end="")
            else:
                print("Решка ", end="")
        if x1+x2+x3 == 3:
            break
        if x1+x2+x3 == 6:
            break
        print("")

coin()