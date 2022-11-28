'''1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0.56 -> 11'''


def sum(num):
    num = int(num)
    print(number)
    sum = 0
    temp = 0
    while num > 10:    
            sum += num % 10
            num = num // 10
    if num < 10:
        sum+= num
    return sum


print('Введите число: ')
number = input().replace('.', '')
print(sum(number))

