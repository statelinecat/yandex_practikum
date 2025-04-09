from itertools import count

b, f, st = (float(x) for x in input().split())
for i in count(b, st):
    if i <= f:
        print(i)
    else:
        break