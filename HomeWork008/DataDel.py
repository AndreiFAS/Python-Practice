def start():
    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork008\BD.csv', 'r', encoding='utf-8') as file:
        lst = (''.join(file)).split('\n')
        res = []
        findData = input('Введите данные удаляемого сотрудника: ').lower()
        for i in lst:
            if i.find(findData) < 0:
                res.append(i)

    with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork008\BD.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(res))