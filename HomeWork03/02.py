'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''
from random import randint

def create_list(min, max, amount):
    if min > max:
        temp = max
        max = min
        min = temp
    arr = []
    i = 0
    while i < amount:
        rnd = randint(min, max)
        arr.append(rnd)
        i += 1
    return(arr)


def show_list():
    print('Введите размер списка: ')
    size = int(input())
    print('Введите диапазон значений элементов от минимального до максимального: ')
    minimal = int(input())
    maximal = int(input())
    lst = create_list(minimal, maximal, size)
    print(lst)
    return(lst)


def math_list(lst):
    list_res = []
    result = 0
    first = 0
    last = -1
    for i in range(len(lst) // 2):
        result = lst[first] * lst[last]
        list_res.append(result)
        first += 1
        last -= 1
        result = 0
    if len(lst) % 2 != 0:
        list_res.append(lst[(len(lst) // 2) + 1])
    return list_res


list_1 = show_list()
print(f' Произведение парных элементов равняется {math_list(list_1)}')

