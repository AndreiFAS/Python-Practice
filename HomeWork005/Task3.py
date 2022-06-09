# Создайте программу для игры в "Крестики-нолики".

from copy import deepcopy


def win_condition(lst):
    if (lst[0][0] == lst[0][1] == lst[0][2] == '+'
        or lst[1][0] == lst[1][1] == lst[1][2] == '+'
        or lst[2][0] == lst[2][1] == lst[2][2] == '+'
        or lst[0][0] == lst[1][0] == lst[2][0] == '+'
        or lst[0][1] == lst[1][1] == lst[2][1] == '+'
        or lst[0][2] == lst[1][2] == lst[2][2] == '+'
        or lst[0][0] == lst[1][1] == lst[2][2] == '+'
            or lst[2][0] == lst[1][1] == lst[0][2] == '+'):
        print('Победили +')
    elif (lst[0][0] == lst[0][1] == lst[0][2] == '0'
          or lst[1][0] == lst[1][1] == lst[1][2] == '0'
          or lst[2][0] == lst[2][1] == lst[2][2] == '0'
          or lst[0][0] == lst[1][0] == lst[2][0] == '0'
          or lst[0][1] == lst[1][1] == lst[2][1] == '0'
          or lst[0][2] == lst[1][2] == lst[2][2] == '0'
          or lst[0][0] == lst[1][1] == lst[2][2] == '0'
          or lst[2][0] == lst[1][1] == lst[0][2] == '0'):
        print('Победили 0')
    else:
        print('Ничья')


def print_field(lst):
    print(lst[0])
    print(lst[1])
    print(lst[2])


# def game(lst):
#     while ' ' not in lst:
#         a, b = int(eval(input()))
#         lst[a][b] = '+'
#         print_field(lst)



start_field = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

game_field = deepcopy(start_field)

game(game_field)
win_condition(game_field)
