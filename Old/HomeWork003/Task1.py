# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

task_list = [2, 3, 5, 9, 3, 45, 12, 11]


def uneven_summ(list):
    result = 0
    for i in range(len(list)):
        if i % 2 != 0:
            result += list[i]
    return result


print(task_list)
print(uneven_summ(task_list))
