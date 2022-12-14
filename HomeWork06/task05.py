'''2* Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;'''

expression = '96-6/(3+7)*4+(-7)'
exit()
def operation(exp):
    res = []
    answer = 0
    arr_of_index_int = [int(i) for i in range(len(exp)) if exp[i].isdigit()]
    print(arr_of_index_int)

    for i in range(len(arr_of_index_int) - 1):
        if arr_of_index_int[i + 1] - arr_of_index_int[i] == 1:
            res.append(exp[arr_of_index_int[i]] + exp[arr_of_index_int[i + 1]])
        elif arr_of_index_int[i + 1] - arr_of_index_int[i] >= 2:
            res.append(exp[arr_of_index_int[i + 1]])
    print(res)

    open_bracket = res.index('(')
    close_bracket = res.index(')')

    for j in range(len(exp)):
        if j > open_bracket and j < close_bracket:
            if exp[j].isdigit():
                answer

    




    # for item in range(len(exp)):
    #     if exp[item] == '*':



    # answer = sum(res)
    # print(answer)

    # for k in range(open_bracket + 1, close_bracket - 1):
    #     res.pop(k)
    


operation(expression)
