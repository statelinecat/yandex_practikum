from itertools import product

n = int(input())
m = int(input())
width = len(str(n * m))
rect = list(product(range(n), range(m)))
for i, j in rect:
    print(f"{i * m + j + 1:>{width}}", end=" ")
    if j == m - 1:
        print()
