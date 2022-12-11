'''1 предложить улучшения кода для четырёх уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
Начиная с 3 семинара.
______________________________________________________________________________________________________________________________
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''
#Zip

lst = [2, 3, 4, 5, 6, 7, 17]

def devide(ls):
    size = len(ls)
    size = int(size // 2)
    temp = []
    res = []
    for i in range(size):
        temp.append(ls[i])
    j = size + 1
    while j != len(ls):
        res.append(ls[j])
        j += 1
    res = res[::-1]
    result = list(zip(temp, res))
    #print(temp)
    #print(res)
    return result

list_zip = devide(lst)
print(list_zip)

for i in range(len(list_zip)):
    num = list_zip[i]
    num = num[0] * num[1]
    print(num)

if len(lst) % 2 == 1:    
    s = len(lst) // 2
    print(lst[s])

