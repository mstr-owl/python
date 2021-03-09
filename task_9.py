# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

COUNT_EL = 5
ROW = 4
a = []
for i in range(ROW):
    b = []
    for j in range(COUNT_EL):
        number = int(random() * 200)
        b.append(number)
        print(f'{number}', end=' ')
    a.append(b)
    print()

max_num = -1
for j in range(COUNT_EL):
    min_num = 200
    for i in range(ROW):
        if a[i][j] < min_num:
            min_num = a[i][j]
    if min_num > max_num:
        max_num = min_num
print(f'Максимальное число среди минимальных: {max_num}')
