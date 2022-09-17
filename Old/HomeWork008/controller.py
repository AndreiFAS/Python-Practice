import DataRead
import DataAdd
import DataDel
import DataFind



def start():
    x = input('Выберите режим работы с БД:\n1 - просмотр всех записей\n2 - добавить запись\n3 - удалить запись\n4 - найти запись\n')
    if x == '1':
        DataRead.start()
    elif x == '2':
        DataAdd.start()
    elif x == '3':
        DataDel.start()
    elif x == '4':
        DataFind.start()
    else:
        print('Ошибка выбора режима работы с БД!\n')
        start()