'''4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff'''
#RLE01 - исходный файл
#RLE02 - сжатый файл

# Сжатие:

with open ('HomeWork05/RLE01.txt', 'r') as reading_file:
    reading_file = list(map(str, reading_file.read()))
    #print(reading_file)

    
def find_count(lst):
    res = []
    elements = []
    temp = 0
    i = 0
    while i != len(lst):
        if lst[temp] == lst[i]:
            res.append(lst[temp])
        elif lst[temp] != lst[i]:
            if len(res) > 9:
                size = len(res)
                while size > 9:
                    if size % 2 == 0:
                        size = int(size / 2)
                        elements.append(size)
                        elements.append(lst[temp])
                        elements.append(size)
                        elements.append(lst[temp])
                    else:
                        size = int(size // 2 + 1)
                        elements.append(size)
                        elements.append(lst[temp])
                        elements.append(size - 1)
                        elements.append(lst[temp])
            else:
                elements.append(len(res))
                elements.append(lst[temp])
            res = []
            temp = i
            i -= 1
        if i == len(lst) - 1:
            elements.append(len(res))
            elements.append(lst[temp])
        i += 1

    #print(elements)
    return elements


def send(ls):
    text = ''.join(map(str, ls))
    with open ('HomeWork05/RLE02.txt', 'w') as t:
        t.write(text)
    return text


text = find_count(reading_file)
#print(text)
text = send(text)
#print(text)


# Восстановление:

with open ('HomeWork05/RLE02.txt', 'r') as returned_file:
    returned_file = list(map(str, returned_file.read()))
    #print (returned_file)


def create_str(ls_res):
    res = ''
    for i in range(len(ls_res)):
        if ls_res[i].isdigit():
            num = int(ls_res[i])
            temp = ls_res[i + 1] * num
            res += temp
    return res


turned_back = create_str(returned_file)
print(turned_back)
