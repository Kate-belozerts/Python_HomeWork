'''2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]'''

def income_number():
    a = False
    while a == False:
        num = int(input('Введите число: '))
        if num < 1:
            a = False
            print('Введите другое число, нужно натуральное\nт.е. больше ноля :)')
        else: 
            a = True
    return num


def find_nod(num):
    ls = []
    i = 2
    while i <= num:
        if num % i == 0:
            if i == num:
                ls.append(i)
                i += 1
            else:
                num /= i
                #print(num)
                ls.append(i)
        else:
            i += 1
    if len(ls) == 1:
        print('Простое число')
    else:
        print(ls)
    return ls


number = income_number()
find_nod(number)
