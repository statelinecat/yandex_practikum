numbers = [1, 2, 3, 4, 5]
s = {x for x in numbers if (x ** 0.5).is_integer()}
print(s)