# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input("Введите трехзначное число: "))
n1 = number % 10
n2 = number % 100 // 10
n3 = number // 100
sum_number = n1 + n2 + n3
prod = n1 * n2 * n3
print(sum_number)
print(prod)
