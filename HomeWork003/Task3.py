# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

task_list = [1.1, 1.2, 3.1, 5, 10.01]


def task_result(list):
    fraction_list = []
    result = 0
    for i in range(len(list)):
        if type(list[i]) != int:
            fraction_list.append(round((list[i] - int(list[i])), 2))
    print(fraction_list)
    max = fraction_list[0]
    min = fraction_list[0]
    for i in range(len(fraction_list)):
        if fraction_list[i] > max:
            max = fraction_list[i]
        elif fraction_list[i] < min:
            min = fraction_list[i]
    result = max - min
    return result


print(task_result(task_list))
