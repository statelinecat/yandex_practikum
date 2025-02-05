# Чтение входных данных
N = int(input())  # Высота прямоугольника
M = int(input())  # Ширина прямоугольника

# Определяем количество цифр в максимальном числе
max_num = N * M
num_digits = len(str(max_num))

# Построение прямоугольника
current = 1
for i in range(N):
    row = ""
    for j in range(M):
        # Форматируем число с учетом ширины
        row += f"{current:{num_digits}d} "
        current += 1
    # Убираем последний пробел и добавляем перевод строки
    print(row.strip())