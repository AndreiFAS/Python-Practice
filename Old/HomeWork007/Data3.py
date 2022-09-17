# .csv

def start():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите номер телефона: ')
    decription = input('Добавьте описание: ')
    with open('/Old/HomeWork007/BD.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{name};{surname};{telephone};{decription}\n')