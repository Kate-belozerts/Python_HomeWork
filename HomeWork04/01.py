'''1 Вычислить число π c заданной точностью d
*Пример:* 
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''
from math import pi
print(pi)
# Рассчет с помощью ряда Нилаканта

def find_pi():
    d = 0.001
    i = 2
    j = 3
    k = 4
    p = 3 + 4 / (i * j * k)
    while (p - pi) > d:
        i = k
        j += 2
        k += 2
        p -= 4 / (i * j * k)
        i = k
        j += 2
        k += 2
        p += 4 / (i * j * k)
    print(p)


find_pi()
