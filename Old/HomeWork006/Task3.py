# Создайте программу для игры в "Крестики-нолики".

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


def get_step_check_input():
    x = int(input(f'Введите строку(1, 2, 3): '))
    while x != 1 and x != 2 and x != 3:
        print('Ошибка ввода!')
        x = int(input(f'Введите строку(1, 2, 3): '))

    y = int(input(f'Введите столбец(1, 2, 3): '))
    while y != 1 and y != 2 and y != 3:
        print('Ошибка ввода!')
        y = int(input(f'Введите столбец(1, 2, 3): '))

    return x, y


def game():
    start_field = [[' ']*3 for j in range(3)]
    flag = randint(0, 1)  # 1 - 'x', 0 - 'o'
    if flag == 1:
        player = 'x'
    else:
        player = 'o'

    for i in range(9):
        print_field(start_field)

        if player == 'x':
            print('Ходят х')
            x, y = get_step_check_input()
            while start_field[x - 1][y - 1] != ' ':
                print('Эта клетка занята! Выберите свободную!')
                x, y = get_step_check_input()
            start_field[x - 1][y - 1] = player
            player = 'o'
        else:
            print('Ходят o')
            x, y = get_step_check_input()
            while start_field[x - 1][y - 1] != ' ':
                print('Эта клетка занята! Выберите свободную!')
                x, y = get_step_check_input()
            start_field[x - 1][y - 1] = player
            player = 'x'

        if win_condition(start_field) == 'x':
            print_field(start_field)
            print('Победили х!')
            break
        elif win_condition(start_field) == 'o':
            print_field(start_field)
            print('Победили o!')
            break

        i += 1

    if i == 9:
        print_field(start_field)
        print('Победила дружба!')

    restart = input("Если хотите начать игру заново введите 1 ")
    if restart == '1':
        game()

game()
