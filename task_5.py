# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
from random import random

count_number = 20
mus_num = []
for i in range(count_number):
    mus_num .append(int(random() * 100) - 50)
print(mus_num)

i = 0
index = -1
while i < len(mus_num):
    if mus_num[i] < 0 and index == -1:
        index = i
    elif mus_num[index] < mus_num[i] < 0:
        index = i
    i += 1

print(f'максимально отрициательное число: {mus_num [index]}, индекс числа: {index + 1}')
