def start():
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork008\BD.csv', 'r', encoding='utf-8') as file:
        lst = (''.join(file)).split('\n')
        findData = input('Введите данные искомого сотрудника: ').lower()
        for i in lst:
            if i.find(findData) > 0:
                print(i)


