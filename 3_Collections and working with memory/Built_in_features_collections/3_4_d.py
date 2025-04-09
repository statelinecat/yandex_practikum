from itertools import accumulate

string = [x + ' ' for x in input().split()]
for y in accumulate(string):
    print(y)