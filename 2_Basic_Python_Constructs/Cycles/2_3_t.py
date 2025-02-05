def check_blockchain(blocks):
    h_prev = 0  # Начальный хэш h0 = 0

    for i, b in enumerate(blocks):
        # Извлекаем h_n, r_n, m_n из блока b
        h_n = b % 256
        r_n = (b // 256) % 256
        m_n = b // (256 ** 2)

        # Проверяем, что h_n < 100
        if h_n >= 100:
            return i

        # Вычисляем ожидаемый хэш
        h_expected = (37 * (m_n + r_n + h_prev)) % 256

        # Сравниваем с реальным хэшем
        if h_n != h_expected:
            return i

        # Обновляем h_prev для следующего блока
        h_prev = h_n

    # Если все блоки прошли проверку
    return -1

# Ввод данных
N = int(input())
blocks = [int(input()) for _ in range(N)]

# Проверка блокчейна
result = check_blockchain(blocks)

# Вывод результата
print(result)