import emoji


'''3 Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:

 1  |  2  |  3
--------------
 4  |  5  |  6
--------------
 7  |  8  |  9   '''


def game_started():
    smile = emoji.emojize(':grinning_face:')
    think = emoji.emojize(':thinking_face:')
    glasses = emoji.emojize(':nerd_face:')
    anxious = emoji.emojize(':anxious_face_with_sweat:')
    table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = int(input(f'Хотите играть крестиками - тогда введите 1\nА если ноликами, то введите ноль {smile}\n'))
    count = 9
    result = False
    who_you_are = int(input('Скажите, за кого будете играть?\n'\
                        'Как программист введите - 1\n'\
                        'За стихии - 2\n'\
                        'Животный мир - 3\n'))
    while count != 0 and result is False:
        if player == 1:
            show_table(table)
            number = int(input(f'На какую цифру хотите поставить свой значок? {think}{anxious}'))
            table = players_turn(number, table, player, who_you_are)
            player = 0
        else:
            show_table(table)
            number = int(input(f'На какую цифру хотите поставить значок соперника? {glasses}{anxious}'))
            table = players_turn(number, table, player, who_you_are)
            player = 1
        result = winner(table)
        count -= 1
    if result is True:
        thumb = emoji.emojize(':thumbs_up:')
        print('Игра завершена' + thumb)


def players_turn(num, ls, turn, choice):
    a, b = smiles(choice)
    if turn == 1:
        res = ls.index(num)
        ls[res] = a
    else: 
        res = ls.index(num)
        ls[res] = b
    return ls


def show_table(col):
    minus = emoji.emojize(':minus:')
    print(minus, minus, minus, minus, minus, minus, minus, minus)
    print('')
    print(f'|   {col[0]}   |   {col[1]}   |   {col[2]}   |')
    print(minus, minus, minus, minus, minus, minus, minus, minus + f'\n')
    print(f'|   {col[3]}   |   {col[4]}   |   {col[5]}   |')
    print(minus, minus, minus, minus, minus, minus, minus, minus + f'\n')
    print(f'|   {col[6]}   |   {col[7]}   |   {col[8]}   |')
    print(minus, minus, minus, minus, minus, minus, minus, minus + f'\n')


def winner(col):
    res = False
    party = emoji.emojize(':partying_face:')
    cool = emoji.emojize(':smiling_face_with_sunglasses:')
    star = emoji.emojize(':star-struck:')
    clapp = emoji.emojize(':clapping_hands:')
    while res is False:
        if col[0] == col[1] == col[2]:
            print(f'{col[0]} - Вы выйграли!{party}{clapp}')
            res = True
            break
        elif col[3] == col[4] == col[5]:
            print(f'{col[3]} - Вы выйграли!{cool}{clapp}')
            res = True
            break
        elif col[6] == col[7] == col[8]:
            print(f'{col[6]} - Вы выйграли!{star}{clapp}')
            res = True
            break
        elif col[0] == col[3] == col[6]:
            print(f'{col[0]} - Вы выйграли!{party}{clapp}')
            res = True
            break
        elif col[1] == col[4] == col[7]:
            print(f'{col[1]} - Вы выйграли!{cool}{clapp}')
            res = True
            break
        elif col[2] == col[5] == col[8]:
            print(f'{col[2]} - Вы выйграли!{star}{clapp}')
            res = True
            break
        elif col[0] == col[4] == col[8]:
            print(f'{col[0]} - Вы выйграли!{party}{clapp}')
            res = True
            break
        elif col[2] == col[4] == col[6]:
            print(f'{col[2]} - Вы выйграли!{star}{clapp}')
            res = True
            break
        else:
            break
    return res


def smiles(choice):
    if choice == 3:
        bone = emoji.emojize(':bone:')
        tongue = emoji.emojize(':tongue:')
        return bone, tongue
    if choice == 2:
        fire = emoji.emojize(':fire:')
        water = emoji.emojize(':water_wave:')
        return fire, water
    elif choice == 1:
        comp = emoji.emojize(':laptop:')
        sleep = emoji.emojize(':ZZZ:')
        return comp, sleep


game_started()
