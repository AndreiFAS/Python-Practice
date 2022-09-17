# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

task_list = [2, 3, 4, 5, 6, 7, 8]


def pair_composition(list):
    i = 0
    r_list = []
    while i < len(list)/2:
        r_list.append(list[i]*list[(len(list)-1)-i])
        i += 1
    return r_list


print(task_list)
print(pair_composition(task_list))
