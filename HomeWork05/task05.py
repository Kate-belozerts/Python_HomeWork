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
