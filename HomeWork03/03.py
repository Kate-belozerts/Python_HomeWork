'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

def create_list():
    print('Введите общее количество элементов: ')
    size = int(input())
    lst = []
    for i in range(size):
        print('Введите число: ')
        lst.append(float(input()))
    print(lst)
    return lst


def difference(lst):
    result = 0
    max = 0
    min = lst[0]
    for i in range(len(lst)):
        lst[i] = (lst[i] % 1) + 1
        #print(lst[i])
        if lst[i] > max:
            max = lst[i]
        if lst[i] < min:
            min = lst[i]
    #print(min, max)
    result = max - min
    return result


list_01 = create_list()
print(f'Разница между максимальной и минимальной дробной частью числа равна: {difference(list_01)}')

