'''4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
from random import randint
# Закомментирован вывод списка коэффициентов в функции create()

def create():
    correct = True
    while correct == True:
        k = int(input('Введите натуральную степень: '))
        if k > 0:
            correct = False
    a = randint(-50, 100) - 17
    b = int(a * 2 // 3) * (-1)
    #for i in range(1, k + 1):
        #print(f'{randint(-100, 100)}x**{i}')        
    k = randint(2, k)
    return (a, b, k)


def print_formula(x_1, x_2, k_1):
    if x_1 > 0 and x_2 > 0:
        return (f'{x_1}X**{k_1} + {x_2}X**{k_1} = 0')
    elif x_1 < 0 and x_2 < 0:
        return (f'({x_1}X**{k_1}) {x_2}X**{k_1} = 0')
    elif x_1 > 0 and x_2 < 0:
        return (f'{x_1}X**{k_1} {x_2}X**{k_1} = 0')
    elif x_1 < 0 and x_2 > 0:
        return (f'({x_1}X**{k_1}) + {x_2}X**{k_1} = 0')


x1, x2, k1 = create()
#print(x1, x2, k1)
st = print_formula(x1, x2, k1)

file_formula = open('HomeWork04/formula.txt', 'a')
file_formula.write(st)
file_formula.close()
