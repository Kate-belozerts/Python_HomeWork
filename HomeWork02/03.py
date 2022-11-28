'''3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

*Пример:*

- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072 '''


def sum_of_n(num):
    lst = []
    result = 0
    for i in range(1, num + 1):
        result = ((1 + i) / i)**i
        lst.append(result)
        result = 0
    return(lst)


print('Введите число: ')
number = int(input())
print(sum_of_n(number))

