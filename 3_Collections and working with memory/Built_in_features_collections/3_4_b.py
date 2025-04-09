a = input().split(", ")
b = input().split(", ")
for x, y in zip(a, b):
    print(f"{x} - {y}")