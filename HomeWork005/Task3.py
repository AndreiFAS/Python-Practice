# Создайте программу для игры в "Крестики-нолики".

from copy import deepcopy
from random import randint


def win_condition(lst):
    if (lst[0][0] == lst[0][1] == lst[0][2] == 'x'
        or lst[1][0] == lst[1][1] == lst[1][2] == 'x'
        or lst[2][0] == lst[2][1] == lst[2][2] == 'x'
        or lst[0][0] == lst[1][0] == lst[2][0] == 'x'
        or lst[0][1] == lst[1][1] == lst[2][1] == 'x'
        or lst[0][2] == lst[1][2] == lst[2][2] == 'x'
        or lst[0][0] == lst[1][1] == lst[2][2] == 'x'
            or lst[2][0] == lst[1][1] == lst[0][2] == 'x'):
        return 'x'
    elif (lst[0][0] == lst[0][1] == lst[0][2] == 'o'
          or lst[1][0] == lst[1][1] == lst[1][2] == 'o'
          or lst[2][0] == lst[2][1] == lst[2][2] == 'o'
          or lst[0][0] == lst[1][0] == lst[2][0] == 'o'
          or lst[0][1] == lst[1][1] == lst[2][1] == 'o'
          or lst[0][2] == lst[1][2] == lst[2][2] == 'o'
          or lst[0][0] == lst[1][1] == lst[2][2] == 'o'
          or lst[2][0] == lst[1][1] == lst[0][2] == 'o'):
        return 'o'


def print_field(lst):
    print(lst[0])
    print(lst[1])
    print(lst[2])


def game(lst):
    flag = randint(0, 1)  # 1 - 'x', 0 - 'o'
    if flag == 1:
        player = 'x'
    else:
        player = 'o'

    for i in range(9):
        print_field(lst)

        if player == 'x':
            print('Ходят х')
            x = int(input('Введите строку: '))
            y = int(input('Введите столбец: '))
            lst[x][y] = 'x'
            player = 'o'
        else:
            print('Ходят o')
            x = int(input('Введите строку: '))
            y = int(input('Введите столбец: '))
            lst[x][y] = 'o'
            player = 'x'
        i += 1

        if win_condition(lst) == 'x':
            print('Победили х!')
            break
        elif win_condition(lst) == 'o':
            print('Победили o!')
            break
    if i == 9:
        print('Победила дружба!')


start_field = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

game_field = deepcopy(start_field)

game(game_field)