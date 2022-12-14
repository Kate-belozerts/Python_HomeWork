'''1 предложить улучшения кода для четырёх уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Начиная с 3 семинара.
______________________________________________________________________________________________________________________________
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
#List Comprehension

lst = [2, 3, 5, 9, 3, 2, 3, 5, 9, 3]

lst = [lst[i] for i in range(len(lst)) if i % 2 == 1]
print(lst)
print(sum(lst))


# Было: 
# from random import randint

# def create_list(min, max, amount):
#     if min > max:
#         temp = max
#         max = min
#         min = temp
#     arr = []
#     i = 0
#     while i < amount:
#         rnd = randint(min, max)
#         arr.append(rnd)
#         i += 1
#     return(arr)


# def show_list():
#     print('Введите размер списка: ')
#     size = int(input())
#     print('Введите диапазон значений элементов от минимального до максимального: ')
#     minimal = int(input())
#     maximal = int(input())
#     lst = create_list(minimal, maximal, size)
#     print(lst)
#     return(lst)


# def sum_of_num(lst):
#     sum = 0
#     for i in range(1, len(lst) - 1, 2):
#         sum += lst[i] 
#     return(sum)


# list_1 = show_list()
# result = sum_of_num(list_1)
# print(f'Сумма элементов на нечетных позициях равна: {result}')

