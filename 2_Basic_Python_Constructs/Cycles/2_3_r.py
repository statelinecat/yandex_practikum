number = int(input())
encrypted_number = ''

factors = []  # Список для хранения простых множителей
divisor = 2   # Начинаем с наименьшего простого числа

while number > 1:
    # Пока число делится на текущий делитель, добавляем его в список
    while number % divisor == 0:
        factors.append(divisor)
        number //= divisor
    # Переходим к следующему делителю
    divisor += 1

# Вывод результата в формате "a * b * c * ..."
for factor in factors:
    encrypted_number += str(factor) + ' * '

# Удаление лишней информации
encrypted_number = encrypted_number[:-3]
print(encrypted_number)