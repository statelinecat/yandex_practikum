# Чтение входных данных
N = int(input())  # Высота прямоугольника
M = int(input())  # Ширина прямоугольника

# Определяем количество цифр в максимальном числе
max_num = N * M
num_digits = len(str(max_num))

# Построение прямоугольника
current = 1
for i in range(N):
    row = []
    for j in range(M):
        # Форматируем число с учетом ширины и добавляем в список
        row.append(f"{current:>{num_digits}}")
        current += 1
    # Соединяем числа в строку с пробелами между ними
    print(" ".join(row))


