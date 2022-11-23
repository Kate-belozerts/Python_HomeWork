## Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
from random import randint

x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)

if not(x or y or z) == (not x and not y and not z):
    print('Equal')
else:
    print('Not equal')

print(x, y, z)

