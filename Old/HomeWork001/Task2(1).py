#1. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list_bool = [1, 1, 1,
             0, 0, 0,
             1, 1, 0,
             1, 0, 1,
             0, 1, 1,
             0, 0, 1,
             0, 1, 0,
             1, 0, 0]

i = 0

while i < len(list_bool):
    print(not(list_bool[i] or list_bool[i+1] or list_bool[i+2]) ==
          ((not(list_bool[i])) and (not(list_bool[i+1])) and (not(list_bool[i+2]))))
    i += 3
