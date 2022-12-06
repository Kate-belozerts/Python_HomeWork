'''5 Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. 
Степени многочленов могут отличаться.'''
# Генерирование второй формулы из предыдущего файла:

from task04 import create
from task04 import print_formula

x1, x2, k = create()
string_02 = print_formula(x1, x2, k)

path_01 = 'HomeWork04/formula.txt'
path_02 = 'HomeWork04/file_02.txt'

file_sec = open(path_01, 'w')
file_sec.write(string_02)
file_sec.close()

# Считывание формулы:

def reading(way):
    read_file = open(way, 'r')
    for i in read_file:
        res = i
    read_file.close()
    return res


def to_string(st):
    lst = []
    for i in range(len(st) - 1):
        if st[i].isdigit() and st[i + 1].isdigit():
            if st[i - 1] == '-':
                temp = (st[i] + st[i + 1])
                lst.append('-' + temp)
            else:
                lst.append(st[i] + st[i + 1])
            
        elif st[i].isdigit() and st[i - 1] == '*':
            lst.append(st[i])
    return lst


formula_01 = str(reading(path_01))
formula_02 = str(reading(path_02))
print(formula_01, '   and   ', formula_02)

res_01 = to_string(formula_01)
res_02 = to_string(formula_02)
#print(res_01, '    and    ', res_02)

# Сложение: (К сожалению работает только если Х - двузначное число((((((.. )

def make_sum(list_01, list_02):
    temp = 0
    temp2 = 0
    if list_01[1] == list_02[1]:
        temp = int(list_01[0] + list_02[0]) 
    if list_01[3] == list_02[3]:
        temp2 = int(list_01[2] + list_02[2])
    
    # Простите меня за это, я честно не хотела так))....но дедлайн слишком близко
    if temp == 0 and temp2 == 0:
        return (f'{list_01[0]}X**{list_01[1]}+{list_02[0]}X**{list_02[1]}+{list_01[2]}X**{list_01[3]}+{list_02[2]}X**{list_02[3]} = 0')
    if temp != 0 and temp2 == 0:
        return (f'{temp}X**{list_01[1]}+{list_01[2]}X**{list_01[3]}+{list_02[2]}X**{list_02[3]} = 0')
    if temp == 0 and temp2 != 0:
        return (f'{list_01[0]}X**{list_01[1]}+{list_02[0]}X**{list_02[1]}+{temp2}X**{list_01[3]} = 0')


def change_plus(st):
    st = list(st)
    end = ''
    for i in range(len(st)):
        if st[i] == '+' and st[i + 1] == '-':
            st[i] = ' '
    for j in range(len(st)):
        end += st[j]
    return end
    

resultische = make_sum(res_01, res_02)
end_result = change_plus(resultische)
print(end_result)

# Вывод суммы в отдельный файл:

result_file = open('HomeWork04/result_file.txt', 'w')
result_file.write(end_result)
result_file.close()
