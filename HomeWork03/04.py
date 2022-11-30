'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

def turn_to_bin(num):
    res = []
    while num != 0:
        if num % 2 == 0:
            res.append(0)
            num = num // 2
        elif num % 2 == 1:
            res.append(1)
            num = num // 2  
    res = change_order(res)  
    result = to_string(res)
    return result


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


def to_string(arr):
    st = ''
    for i in range(len(arr)):
        st += f'{arr[i]}'
    return st


print('Введите число: ')
number = int(input())
print(f' Число {number} в двоичной системе счисления равняется: {turn_to_bin(number)}')

