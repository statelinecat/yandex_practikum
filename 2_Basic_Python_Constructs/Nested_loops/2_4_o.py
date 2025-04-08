# Чтение входных данных
n = int(input())  # Высота прямоугольника
m = int(input())  # Ширина прямоугольника

# Определяем количество цифр в максимальном числе
max_num = n * m
num_digits = len(str(max_num))
for i in range(n):
    row = []
    for j in range(m):
        if j % 2 == 0:
            num = j * n + i + 1
        else:
            num = (j + 1) * n - i
        row.append(f"{num:>{num_digits}}")
    print(" ".join(row))