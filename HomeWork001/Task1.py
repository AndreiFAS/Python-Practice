# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите день недели "))
if a < 1 or a > 7:
    print("Неправильное число!")
elif a > 5:
    print("да")
else:
    print("нет")