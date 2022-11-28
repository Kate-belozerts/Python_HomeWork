'''4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.'''

from random import randint


def create(num):
    lst = []
    for i in range(num):
        lst.append(randint(-num, num + 1))
    return lst


def result(index_a, index_b, list_elements):
    a = list_elements[index_a]
    b = list_elements[index_b]
    res = a * b
    return res


print('Введите число: ')
element = int(input())

print('Введите два номера позиции: ')
position_first = int(input())
position_second = int(input())

array = create(element)
print(array)
print(result(position_first, position_second, array))

