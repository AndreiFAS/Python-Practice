# БД в формате .csv

def start():
    name = input('Имя: ').lower()
    surname = input('Фамилию: ').lower()
    company = input('Название компании: ').lower()
    position = input('Должность: ').lower()
    telephone = input('Номер телефона: ').lower()
    with open('/Old/HomeWork008/BD.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{name};{surname};{company};{position};{telephone}\n')