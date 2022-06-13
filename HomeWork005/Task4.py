# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def RLEcompres(txt):    
    buffer = []
    for i in txt:
        if (len(buffer) == 0):
            buffer.append([1, i])
        else:
            if buffer[len(buffer) - 1][1] == i:
                buffer[len(buffer) - 1][0] += 1
            else:
                buffer.append([1, i])
    result = ''
    for i in buffer:
        result += ''.join(map(str, i))
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


txt = 'vvbbssssstttttttt'  

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork005\Text.txt', 'w+') as data:
    data.write(txt)

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork005\TextC.txt', 'w+') as data:
    data.write(RLEcompres(txt))

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork005\TextC.txt', 'r', encoding='utf-8') as data:
    comp_txt = data.read()

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork005\TextR.txt', 'w+') as data:
    data.write(RLErecover(comp_txt))

