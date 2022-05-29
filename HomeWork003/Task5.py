# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = 10
fib_list = []


def fibonacci(n) -> list:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    f_list = fibonacci(n-1)
    f_list.append(f_list[-1] + f_list[-2])
    return f_list


f_list = fibonacci(n)
fib_list = f_list.copy()
fib_list.insert(0, 0)
for i, fib in enumerate(f_list):
    if i % 2 != 0:
        fib_list.insert(0, f_list[i]*(-1))
    else:
        fib_list.insert(0, f_list[i])

print(fib_list)