# Задана натуральная степень n. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени пример записи
# в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0


import random


def get_polylist(n):
    poly_list = []
    while n > 1:
        poly_list.append(str(random.randint(1, 100)) + 'x^' + str(n) + ' + ')
        n -= 1
    poly_list.append(str(random.randint(1, 100)) + 'x' + ' + ')
    poly_list.append(str(random.randint(1, 100)) + ' = 0')
    return poly_list


k = random.randint(2, 10)
task_str = ''.join(get_polylist(k))

print(task_str) # проверка в консоли

with open('/Old/HomeWork004/Task4(1).txt', 'w') as data:
    data.write(task_str)

# для 5ой задачи
k = random.randint(2, 10)
task_str = ''.join(get_polylist(k))

print(task_str) # проверка в консоли

with open('/Old/HomeWork004/Task4(2).txt', 'w') as data:
    data.write(task_str)
