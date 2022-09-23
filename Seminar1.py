# По двум заданным числам проверить является ли одно квадратом второго
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(a ** 2 == b or b ** 2 == a)

# Найти максимальное из пяти чисел
# lst = [1, 3, 5, -1, 22]3
# lst = []
# for i in range(5):
#     num = int(input("Введите число: "))
#     lst.append(num)
#
# res = lst[0]
# for i in range(1, 5):
#     if lst[i] > res:
#         res = lst[i]
# print(res)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# n = int(input("Введите число: "))
# for i in range(-n, n + 1):
#     print(i, end=" ")

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа
# n = float(input("Введите число: "))
# print(int(n * 10) % 10)

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n = int(input("Введите число: "))
# print((n % 5 == 0 and n % 10 == 0) or (n % 15 == 0 and n % 30 != 0))

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'{x, y, z}: {(not (x or y or z)) == (not x and not y and not z)}')

# Сложить числа вещественного числа
# n = input("Введите число: ")
# res = 0
# for i in n:
#     if i != "." and i != ",":
#         res += int(i)
# print(res)

# Написать программу проверки, является ли строка палиндромом
# string = "ab21ba"
# # count = 0
# # for i in range(len(string) // 2):
# #     if string[i] == string[-1 - i]:
# #         count += 1
# #
# # if count == len(string) // 2:
# #     print("Polindrom!")
# # else:
# #     print("No!!!")
#
# rev_string = string[::-1]
# print(string == rev_string)

# Напишите программу, которая выводит нечетные числа из заданного списка и останавливается, если встречает число 554.
# lst = [23, 4, 67, -2, 5, 554, 765]
# for i in lst:
#     if i % 2 != 0 and i != 554:
#         print(i, end=" ")
#     elif i == 554:
#         break
