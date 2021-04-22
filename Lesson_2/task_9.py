# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
numbers = int(input('Введите числа, для прекращения ввода чисел введите 0: '))
max_sum = 0
max_number = 0
while numbers != 0:
    n = numbers
    z = 0
    while numbers > 0:
        z += numbers % 10
        numbers //= 10
    if z > max_sum:
        max_sum = z
        max_number = n
    numbers = int(input())
print(f'Число {max_number} имеет максимальную сумму цифр: {max_sum}')
