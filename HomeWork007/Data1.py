# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2


def start():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите номер телефона: ')
    decription = input('Добавьте описание: ')
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork007\BD1.txt', 'a+', encoding='utf-8') as file:
        file.write('\n'.join([name, surname, telephone, decription]) + '\n')