'''5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint'''

from random import randint


def change_order(arr):
    rnd = randint(0, len(arr))
    for i in range(len(arr) - 1):
        temp = arr[i]
        arr[i] = arr[rnd]
        arr[rnd] = temp
    return arr


lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
print(change_order(lst))

