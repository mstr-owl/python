# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import random

count_number = 20
mus_num = [0] * count_number
for i in range(count_number):
    mus_num[i] = int(random()*50)
    print(f'{mus_num[i]}', end=' ')
print()

min_ind = 0
max_ind = 0
for i in range(1, len(mus_num)):
    if mus_num[i] < mus_num[min_ind]:
        min_ind = i
    elif mus_num[i] > mus_num[max_ind]:
        max_ind = i
print(f'минимальное число: {mus_num[min_ind]}, максимальное число: {mus_num[max_ind]}')

if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

sum_num = 0
for i in range(min_ind+1, max_ind):
    sum_num += mus_num[i]
print(f'сумма чисел между {mus_num[max_ind]} и {mus_num[min_ind]} составляет: {sum_num}')
