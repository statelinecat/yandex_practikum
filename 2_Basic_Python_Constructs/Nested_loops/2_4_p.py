# n = int(input())  # Размер таблицы (N x N)
# width = int(input())  # Ширина столбца
#
# # Горизонтальная разделительная линия
# horizontal_line = ("-" + "-" * width) * (n - 1) + "-" * n
#
# for i in range(1, n + 1):
#     # Строим строку с числами
#     row = []
#     for j in range(1, n + 1):
#         num = i * j
#         # Форматируем число: центрируем в ячейке шириной `width`
#         if j < n:
#             cell = f"{str(num):^{width}}" + "|"
#         else:
#             cell = f"{str(num):^{width}}"
#
#         row.append(cell)
#
#     # Выводим горизонтальную линию и строку с числами
#     print(horizontal_line)
#     print("".join(row))
#
# # Закрываем таблицу последней горизонтальной линией
# print(horizontal_line)

n = int(input())
width = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j: ^{width}}", end="")
        if j < n:
            print("|", end="")
        else:
            print()
    if i < n:
        print("-" * (n * (width + 1) - 1))