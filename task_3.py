# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import random

count_number = 20
mus_num = [0] * count_number
for i in range(count_number):
    mus_num[i] = int(random()*100)
    print(mus_num[i], end=' ')
print()

min_number = 0
max_number = 0
for i in range(len(mus_num)):
    if mus_num[i] < mus_num[min_number]:
        min_number = i
    elif mus_num[i] > mus_num[max_number]:
        max_number = i
print(f'arr[{min_number+1}]={mus_num[min_number]} arr[{max_number+1}]={mus_num[max_number]}')
b = mus_num[min_number]
mus_num[min_number] = mus_num[max_number]
mus_num[max_number] = b

for i in range(len(mus_num)):
    print(mus_num[i], end=' ')
print()
