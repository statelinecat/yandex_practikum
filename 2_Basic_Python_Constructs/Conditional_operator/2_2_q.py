# Ввод коэффициентов
a = float(input())
b = float(input())
c = float(input())

# Случай 1: все коэффициенты равны нулю
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")

# Случай 2: a и b равны нулю, но c != 0
elif a == 0 and b == 0:
    print("No solution")

# Случай 3: a = 0, уравнение линейное
elif a == 0:
    x = -c / b
    print(f"{x:.2f}")

# Случай 4: a != 0, квадратное уравнение
else:
    D = b**2 - 4 * a * c  # Дискриминант

    if D > 0:  # Два корня
        x1 = (-b - D**0.5) / (2 * a)
        x2 = (-b + D**0.5) / (2 * a)
        # Сортируем корни по возрастанию
        if x1 > x2:
            x1, x2 = x2, x1
        print(f"{x1:.2f} {x2:.2f}")

    elif D == 0:  # Один корень
        x = -b / (2 * a)
        print(f"{x:.2f}")

    else:  # Нет действительных корней
        print("No solution")