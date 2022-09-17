# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))

def dec_to_bin(n, res: list):
    if n == 0:
        return res
    else:
        res.insert(0, n % 2)
        return dec_to_bin(n // 2, res)


print(''.join(str(e) for e in (dec_to_bin(n, res=[]))))
