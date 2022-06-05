# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)


def poly_sum(lst1, lst2):
    res_lst = []
    if len(lst1) > len(lst2):
        j = 0
        for i in range(0, len(lst1[:-2])):
            if lst1[i][-1] != lst2[j][-1]:
                res_lst.append(lst1[i])
            else:
                res_lst.append(
                    str(int(lst1[i][:-3]) + int(lst2[j][:-3])) + 'x^' + lst1[i][-1])
                j += 1
    else:
        j = 0
        for i in range(0, len(lst2[:-2])):
            if lst2[i][-1] != lst1[j][-1]:
                res_lst.append(lst2[i])
            else:
                res_lst.append(
                    str(int(lst2[i][:-3]) + int(lst1[j][:-3])) + 'x^' + lst2[i][-1])
                j += 1
    res_lst.append(str(int(lst1[-2][:-1]) + int(lst2[-2][:-1])) + 'x')
    res_lst.append(str(int(lst1[-1][:-4]) + int(lst2[-1][:-4])) + ' = 0')
    return res_lst


with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork004\Task4(1).txt', 'r') as data:
    poly_str1 = data.read()

print(f'Первый многочлен\t{poly_str1}')
poly_list1 = poly_str1.split(" + ")

with open('D:\GB\Знакомство с языком Python\Python-Practice\HomeWork004\Task4(2).txt', 'r') as data:
    poly_str2 = data.read()

print(f'Второй многочлен\t{poly_str2}')
poly_list2 = poly_str2.split(" + ")

task_str = ' + '.join(poly_sum(poly_list1, poly_list2))

print(f'Сумма многочленов\t{task_str}')
