# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import random

count_number = 10
mus_num = []
for i in range(count_number):
    mus_num.append(int(random() * 100))
    print(f'{mus_num[i]}', end=' ')
print()

if mus_num[0] > mus_num[1]:
    min_num1 = 0
    min_num2 = 1
else:
    min_num1 = 1
    min_num2 = 0

for i in range(2, len(mus_num)):
    if mus_num[i] < mus_num[min_num1]:
        x = min_num1
        min_num1 = i
        if mus_num[x] < mus_num[min_num2]:
            min_num2 = x
    elif mus_num[i] < mus_num[min_num2]:
        min_num2 = i

print(f'Первое минимальное число: {mus_num[min_num1]} индекс числа: {(min_num1 + 1)}')
print(f'Второе минимальное число: {mus_num[min_num2]} индекс числа: {(min_num2 + 1)}')
