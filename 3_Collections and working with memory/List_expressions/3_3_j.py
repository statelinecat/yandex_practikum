rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
s = ''.join([x * y for x, y in rle])
print(s)