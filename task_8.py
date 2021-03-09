# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
COUNT_EL = 5
ROW = 4
a = []
for i in range(ROW):
    b = []
    x = 0
    print(f'{i}-я строка:')
    for j in range(COUNT_EL - 1):
        number = int(input())
        x += number
        b.append(number)
    b.append(x)
    a.append(b)

for i in a:
    print(i)
