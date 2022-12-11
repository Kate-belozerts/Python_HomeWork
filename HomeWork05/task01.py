'''1 Напишите программу, удаляющую из файла все слова, содержащие "абв".'''

with open ('HomeWork05/file01.txt', 'r', encoding = 'utf-8') as file:
    file = list(map(str, file.read().split()))
    print('Исходный текст: ', file)

find = 'абв'
file = filter(lambda x: find not in x, file)
print('Результат: ', *file)
