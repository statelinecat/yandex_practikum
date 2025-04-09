numbers = {15, 49, 36}
s = {x: [y for y in range(1, x + 1) if x % y == 0] for x in numbers}
print(s)