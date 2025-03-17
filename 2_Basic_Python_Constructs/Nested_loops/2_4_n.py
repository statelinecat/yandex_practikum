# Чтение входных данных
N = int(input())  # Высота прямоугольника
M = int(input())  # Ширина прямоугольника

# Инициализация прямоугольника
rectangle = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(0)
    rectangle.append(row)

# Заполнение прямоугольника числами
current = 1
for j in range(M):  # Итерируем по столбцам
    for i in range(N):  # Итерируем по строкам
        rectangle[i][j] = current
        current += 1

# Определяем количество цифр в максимальном числе
max_num = N * M
num_digits = len(str(max_num))

# Вывод прямоугольника
for i in range(N):
    row = []
    for j in range(M):
        # Форматируем число с выравниванием по правому краю и одинаковой шириной
        # row += f"{rectangle[i][j]:>{num_digits}d} "
        row.append(f"{rectangle[i][j]:>{num_digits}}")

    print(" ".join(row))