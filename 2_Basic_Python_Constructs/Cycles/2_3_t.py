# Ввод данных
N = int(input())
blocks = []
for i in range(N):
    blocks.append(int(input()))

h_prev = 0  # Начальный хэш h0 = 0
result = -1  # По умолчанию все блоки валидны

for i, b in enumerate(blocks):
    # Извлекаем h_n, r_n, m_n из блока b
    h_n = b % 256
    r_n = (b // 256) % 256
    m_n = b // (256 ** 2)

    # Проверяем, что h_n < 100
    if h_n >= 100:
        result = i
        break  # Прерываем цикл, так как нашли невалидный блок

    # Вычисляем ожидаемый хэш
    h_expected = (37 * (m_n + r_n + h_prev)) % 256

    # Сравниваем с реальным хэшем
    if h_n != h_expected:
        result = i
        break  # Прерываем цикл, так как нашли невалидный блок

    # Обновляем h_prev для следующего блока
    h_prev = h_n

# Вывод результата
print(result)