# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from ast import Str
from sre_parse import DIGITS
from unicodedata import digit


def RLEcompres(txt):
    buffer = []
    count = 0
    result = ''

    if len(txt) == 1:
        buffer.append(1, txt[0])
    else:
        for i in range(len(txt)):
            count += 1
            if (i + 1) == len(txt) or txt[i] != txt[i + 1]:
                buffer.append(str(count))
                buffer.append(txt[i])
                count = 0

    result += ''.join(buffer)
    return result


def RLErecover(text):
    count = ''
    result = ''
    for i in text:
        if 48 <= ord(i) <= 57:
            count += i
        else:
            for z in range(int(count)):
                result += i
            count = ''
    return result


txt = 'acabbbbeeeee'


with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork006\TextC.txt', 'w+', encoding='utf-8') as data:
    data.write(RLEcompres(txt))

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork006\TextC.txt', 'r', encoding='utf-8') as data:
    comp_txt = data.read()

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork006\TextR.txt', 'w+', encoding='utf-8') as data:
    data.write(RLErecover(comp_txt))

