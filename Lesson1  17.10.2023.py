
import random
chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789+=-!@%&*<>'
lenhth = int(input('Длина пароля? : '))
password=''
for n in range(lenhth):
    password += random.choice(chars)
print(password)


