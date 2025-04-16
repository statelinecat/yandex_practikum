from itertools import chain

num = int(input())
sps = sorted(chain.from_iterable(input().split(', ') for _ in range(num)))
for
print(sps)