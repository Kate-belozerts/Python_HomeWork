'''5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
*Пример:* 
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.'''

numbers = [1, 5, 2, 3, 4, 6, 1, 7]
start = 0
next_element = 1

def sequences(arr, first, second):
    yes = True
    size = len(arr)
    if second == size:
        yes = False
    res = []
    res.append(arr[first])
    while second != size - 1:
        if arr[first] < arr[second]:
            res.append(arr[second])
            print(res)
            first = second
            second += 1
        else:
            second += 1
    if second == size - 1:
        if arr[first] < arr[second]:
            res.append(arr[second])
            print(res)
    # Если активировать то, что ниже (даже 1 из циклов), то индекс second вылетает... (((
    # first = 0
    # while yes:
    #     sequences(arr, first, second + 1)
    # while not yes:
    #     if second != size:
    #         sequences(arr, first + 1, second = first + 1)


sequences(numbers, start, next_element)

## Новое решение:______________________________________________________________

# numbers = [1, 5, 2, 3, 4, 6, 1, 7]
# start = 0
# next_element = 1
 
 
# def sequences(arr, first, second):
#     second_old = second
#     yes = True
#     size = len(arr)
#     if second == size:
#         yes = False
#     res = []
#     res.append(arr[first])
#     while second < size:
#         if res[-1] < arr[second]:
#             res.append(arr[second])
#             print(res)
#             second += 1
#         else:
#             second += 1
 
#     if yes:
#         sequences(arr, first, second_old + 1)
 
 
# for i in range(len(numbers)):
#     sequences(numbers, i, next_element)



# Гениальное решение Сергея через логичную рекурсию: ______________________________________________________________
# from pprint import pprint
 
 
# numbers = [1, 5, 2, 3, 4, 6, 1, 2, 7]
# seq = set()
 
 
# def find_sequences(arr, cur_i=0, cur_seq=tuple()):
#     # Точка выхода: когда индекс вышел за границы списка
#     if cur_i == len(arr):
#         if len(cur_seq) > 1:
#             seq.add(cur_seq)
#         return
 
#     # Ищем дальше, игнорируя текущий элемент
#     find_sequences(arr, cur_i + 1, cur_seq)
 
#     # Ищем дальше, используя текущий элемент, но только если он подходящий
#     if (cur_seq and cur_seq[-1] <= arr[cur_i]) or not(cur_seq):
#         find_sequences(arr, cur_i + 1, cur_seq + (arr[cur_i],))
 
 
# find_sequences(numbers)
 
# pprint(seq)
# print(len(seq))





# Решение Ильи без рекурсии: ______________________________________________________________

# array = [1, 5, 2, 3, 4, 9, 6, 1, 6, 7, 8, 10, 10]

# length = len(array)
# spread_collection = {}
# for i in range(length):
#     spread_collection.update({i: [[array[i]]]})

# print(spread_collection)

# for i in range(length):
#     tmp_item = spread_collection[i]
#     tmp_small_item = []
#     for small_item in tmp_item:
#         for j in range(i + 1, length):
#             if array[j] > small_item[-1]:
#                 tmp_small_item = small_item.copy()
#                 tmp_small_item.append(array[j])
#                 spread_collection[j].append(tmp_small_item)

# tmp_length = 0
# for v in spread_collection:
#     print(v, spread_collection[v])
#     for item in spread_collection[v]:
#         if len(item) > tmp_length:
#             tmp_arr = [item]
#             tmp_length = len(item)
#         elif len(item) == tmp_length:
#             tmp_arr.append(item)
# print(tmp_length)
# print(tmp_arr)
