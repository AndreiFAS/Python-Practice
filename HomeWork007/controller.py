import Data1
import Data2
import Data3
import Data4


def start():
    x = input('Выберите режим записи 1, 2, 3, 4: ')
    if x == '1':
        Data1.start()
    elif x == '2':
        Data2.start()
    elif x == '3':
        Data3.start()
    elif x == '4':
        Data4.start()