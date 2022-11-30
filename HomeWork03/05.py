'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

def fib(num):
    res = 0
    lst_pos = [0, 1]
    lst_otr = [1, -1]
    j = 2
    while res != -num:
        m = j - 1
        n = j - 2
        res = lst_otr[n] - lst_otr[m]
        lst_otr.append(res)
        j += 1
    i = 2
    while res < num:
        m = i - 1
        n = i - 2
        res = lst_pos[m] + lst_pos[n]
        lst_pos.append(res)
        i += 1
    change_order(lst_otr)
    for i in range(len(lst_pos)):
        lst_otr.append(lst_pos[i])
    print(lst_otr)
    return lst_otr

def change_order(str):
    first = 0
    last = -1
    for i in range(len(str) // 2):
        temp = str[first]
        str[first] = str[last]
        str[last] = temp
        first += 1
        last -= 1
    return str


print('Введите число: ')
number = int(input())
list_fib = fib(number)

