
# Чтение входных данных
n = int(input())  # Высота прямоугольника
m = int(input())  # Ширина прямоугольника

# Определяем количество цифр в максимальном числе
max_num = n * m
num_digits = len(str(max_num))
num_ch = 0
num_n_ch = 0
for i in range(n):
    row = []
    if i % 2 == 0:
        num_n_ch = i * m
        for j in range(1, m + 1):
            num_n_ch = num_n_ch + 1
            row.append(f"{num_n_ch:>{num_digits}}")
    else:
        num_ch = num_n_ch + m + 1
        for j in range(1, m + 1):
            num_ch = num_ch - 1
            row.append(f"{num_ch:>{num_digits}}")
    print(" ".join(row))