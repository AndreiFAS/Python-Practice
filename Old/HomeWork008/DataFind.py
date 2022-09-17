def start():
    with open('/Old/HomeWork008/BD.csv', 'r', encoding='utf-8') as file:
        lst = (''.join(file)).split('\n')
        findData = input('Введите данные искомого сотрудника: ').lower()
        for i in lst:
            if i.find(findData) > 0:
                print(i)


