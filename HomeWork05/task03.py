'''3 Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:

 1  |  2  |  3
--------------
 4  |  5  |  6
--------------
 7  |  8  |  9   '''

def game_started():
    table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = int(input('Хотите играть крестиками - тогда введите 1\nА если ноликами, то введите ноль :) '))
    count = 9
    result = False
    while count != 0 and result == False:
        if player == 1:
            show_table(table)
            number = int(input('На какую цифру хотите поставить крестик? '))
            table = players_turn(number, table, player)
            player = 0
        else:
            show_table(table)
            number = int(input('На какую цифру хотите поставить нолик? '))
            table = players_turn(number, table, player)
            player = 1
        result = winner(table)
        count -= 1
    if result == True:
        #show_table(table)
        print('Игра завершена')


def players_turn(num, ls, turn):
    if turn == 1:
        res = ls.index(num)
        ls[res] = 'X'
    else: 
        res = ls.index(num)
        ls[res] = 'O'
    return ls


def show_table(col):
    print('\n_________________________')
    print('')
    print(f'|   {col[0]}   |   {col[1]}   |   {col[2]}   |')
    print('_________________________\n')
    print(f'|   {col[3]}   |   {col[4]}   |   {col[5]}   |')
    print('_________________________\n')
    print(f'|   {col[6]}   |   {col[7]}   |   {col[8]}   |')
    print('_________________________\n')


def winner(col):
    res = False
    while res == False:
        if col[0] == col[1] == col[2]:
            print(f'{col[0]} - Вы выйграли!')
            res = True
            break
        elif col[3] == col[4] == col[5]:
            print(f'{col[3]} - Вы выйграли!')
            res = True
            break
        elif col[6] == col[7] == col[8]:
            print(f'{col[6]} - Вы выйграли!') 
            res = True
            break
        elif col[0] == col[3] == col[6]:
            print(f'{col[0]} - Вы выйграли!') 
            res = True
            break
        elif col[1] == col[4] == col[7]:
            print(f'{col[1]} - Вы выйграли!') 
            res = True
            break
        elif col[2] == col[5] == col[8]:
            print(f'{col[2]} - Вы выйграли!') 
            res = True
            break
        elif col[0] == col[4] == col[8]:
            print(f'{col[0]} - Вы выйграли!') 
            res = True
            break
        elif col[2] == col[4] == col[6]:
            print(f'{col[2]} - Вы выйграли!') 
            res = True
            break
        else: break
    return res


game_started()
