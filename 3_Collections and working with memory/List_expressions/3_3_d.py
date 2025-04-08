numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
s = {x for x in numbers if x % 2 != 0}
print(s)