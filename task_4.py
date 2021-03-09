# 4. Определить, какое число в массиве встречается чаще всего.
from random import random

count_number = 20
mus_num = [0] * count_number
for i in range(count_number):
    mus_num[i] = int(random()*20)
print(mus_num)

number = mus_num[0]
max_count = 1
for i in range(len(mus_num) - 1):
    index_num = 1
    for j in range(i + 1, len(mus_num)):
        if mus_num[i] == mus_num[j]:
            index_num += 1
    if index_num > max_count:
        max_count = index_num
        number = mus_num[i]

if max_count > 1:
    print(f'{max_count} раз(а) встречается число {number}')
else:
    print('Все все числа в массиве уникальны')
