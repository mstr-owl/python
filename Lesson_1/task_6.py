# 6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
number = int(input('Введите Номер буквы в алфавите: '))
letter = ord('a') + number - 1
print(f'Это буква: {chr(letter)}')
