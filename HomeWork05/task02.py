'''2 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"'''
from random import randint


def who_is_first():
    game = 1
    num = int(input(f'Введите любое число:  :) '))
    if num > 7 and num < 77:
        game = 2
    print(f'Первым ходит игрок номер {game}')
    return game


def check_count(num, candy):
    a = True
    if num > 0 and num < 29:
        a = True
    elif candy < 29:
        if num > 0 and num <= candy:
            a = True
    else: a = False
    return a


def switch_player(n):
    if n == 1:
        n = 2
    elif n == 2:
        n = 1
    return n


# Человек против бота поумнее предыдущего: (Человек игрок №1)____________________________________________________________________
def game_with_middle_smartBOT():
    sweet = 117 #2021
    right = True
    player = who_is_first()
    first = []
    second = []

    while right is True and sweet >= 1:
        if player == 1:
            print(f'Ход игрока №{player}')
            print(f'\nОсталось {sweet} конфет ')
            number = int(input('Возьмите порцию конфеток и скажите сколько взяли '))
            right = check_count(number, sweet)

            if right is True: 
                if sweet - number == 0:
                    sweet -= number
                    print(f'Выйглал игрок №{player}')
                else: sweet -= number
                
                first.append(number)
                player = switch_player(player)

            elif right is False:
                print('\nНет-нет.. порция не может быть больше 28 конфет, \
но и совсем без конфет уйти нельзя, даже если вы на диете :(\n \
Либо вы неправильно посчитали остаток)) Попробуйте еще раз: \n')
                right = True
        elif player == 2:
            print(f'Ход игрока №{player}')
            print(f'\nОсталось {sweet} конфет ')
            number = randint(1, 28)
            if not sweet % 28 and sweet > 28 < 50:
                number = 27
            if sweet <= 28:
                number = sweet
            print(f'\nЯ забрал {number} конфет!\n')
            if sweet - number == 0:
                sweet -= number
                print(f'Выйглал игрок №{player}')
            sweet -= number
            second.append(number)
            player = switch_player(player)


    first = list(enumerate(first))
    second = list(enumerate(second))
    print (f'Ходы игрока №1 - {first} \nХоды игрока №2 - {second}')


winner = game_with_middle_smartBOT()
 

quit()
# Человек против глупого бота: (Человек игрок №1) ____________________________________________________________________
def game_against_comp():
    sweet = 2021
    right = True
    player = who_is_first()
    first = []
    second = []

    while right is True and sweet >= 1:
        if player == 1:
            print(f'Ход игрока №{player}')
            print(f'\nОсталось {sweet} конфет ')
            number = int(input('Возьмите порцию конфеток и скажите сколько взяли '))
            right = check_count(number, sweet)

            if right is True: 
                if sweet - number == 0:
                    sweet -= number
                    print(f'Выйглал игрок №{player}')
                else: sweet -= number
                
                first.append(number)
                player = switch_player(player)

            elif right is False:
                print('\nНет-нет.. порция не может быть больше 28 конфет, \
но и совсем без конфет уйти нельзя, даже если вы на диете :(\n \
Либо вы неправильно посчитали остаток)) Попробуйте еще раз: \n')
                right = True
        elif player == 2:
            print(f'Ход игрока №{player}')
            if sweet > 28:
                number = randint(1, 28)
                print(f'\nЯ забрал {number} конфет!\n')
                sweet -= number
            elif sweet <= 28:
                number = randint(1, sweet)
                if sweet - number == 0:
                    sweet -= number
                    print(f'Выйглал игрок №{player}')
            second.append(number)
            player = switch_player(player)


    first = list(enumerate(first))
    second = list(enumerate(second))
    print (f'Ходы игрока №1 - {first} \nХоды игрока №2 - {second}')


winner = game_against_comp()


# Человек против человека: ____________________________________________________________________
def game():
    sweet = 2021
    right = True
    player = who_is_first()
    first = []
    second = []

    while right is True and sweet >= 1:
        print(f'Ход игрока №{player}')
        print(f'\nОсталось {sweet} конфет ')
        number = int(input('Возьмите порцию конфеток и скажите сколько взяли '))
        right = check_count(number, sweet)

        if right is True: 
            if sweet - number == 0:
                sweet -= number
                print(f'Выйглал игрок номер {player}')
            else: sweet -= number
            if player == 1:
                first.append(number)
            else: second.append(number)

            player = switch_player(player)

        elif right is False:
            print('\nНет-нет.. порция не может быть больше 28 конфет, \
но и совсем без конфет уйти нельзя, даже если вы на диете :(\n \
Либо вы неправильно посчитали остаток)) Попробуйте еще раз: \n')
            right = True

    first = list(enumerate(first))
    second = list(enumerate(second))
    print (f'Ходы игрока №1 - {first}, \nХоды игрока №2 - {second}')


winner = game()
