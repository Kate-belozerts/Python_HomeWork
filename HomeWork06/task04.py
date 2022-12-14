'''1 предложить улучшения кода для четырёх уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Начиная с 3 семинара.
______________________________________________________________________________________________________________________________
3 Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]'''
# Filter и Lambda

numbers = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

def numbers_sort(lst):
    list_end = []
    test = set()
    j = 0
    i = j + 1
    while j != len(lst) - 1:
        while i != len(lst):
            if lst[j] == lst[i]:
                test.add(lst[j])
            i += 1
        j += 1
        i = j + 1
    else:
        list_end = list(filter(lambda x: x not in test, lst))
    print(list_end)
    return list_end


result = numbers_sort(numbers) 
print(result)


# Было:

# def create_array():    
#     number = input('Введите числа через пробел: ').split()
#     list_in = []
#     for i in range(len(number)):
#         if number[i].isdigit():
#             list_in.append(int(number[i]))
#     print(list_in)
#     return list_in


# def arr_sort(lst):
#     list_end = []
#     test = set()
#     j = 0
#     i = j + 1
#     while j != len(lst) - 1:
#         while i != len(lst):
#             if lst[j] == lst[i]:
#                 test.add(lst[j])
#             i += 1
#         j += 1
#         i = j + 1
#     else:
#         for k in range(len(lst) - 1):
#             if lst[k] not in test:
#                 list_end.append(lst[k])
#     print(list_end)
#     return list_end
 

# list01 = create_array()
# list02 = arr_sort(list01)
# #list01 = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

