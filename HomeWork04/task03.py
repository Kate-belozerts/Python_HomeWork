'''3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]'''


def create_array():    
    number = input('Введите числа через пробел: ').split()
    list_in = []
    for i in range(len(number)):
        if number[i].isdigit():
            list_in.append(int(number[i]))
    print(list_in)
    return list_in


def arr_sort(lst):
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
        for k in range(len(lst) - 1):
            if lst[k] not in test:
                list_end.append(lst[k])
    print(list_end)
    return list_end
 

list01 = create_array()
list02 = arr_sort(list01)
#list01 = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

