# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите количество чисел в ряду: '))
number = 1
sum_number = 0
for i in range(n):
    sum_number += number
    number /= -2
print(f'сумму {n} чисел: {sum_number}')
