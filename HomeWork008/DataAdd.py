# БД в формате .csv

def start():
    name = input('Имя: ').lower()
    surname = input('Фамилию: ').lower()
    company = input('Название компании: ').lower()
    position = input('Должность: ').lower()
    telephone = input('Номер телефона: ').lower()
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork008\BD.csv', 'a+', encoding='utf-8') as file:
        file.write(f'{name};{surname};{company};{position};{telephone}\n')