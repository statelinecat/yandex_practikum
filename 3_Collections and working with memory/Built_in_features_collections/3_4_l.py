from itertools import chain

n = int(input())
sps = chain.from_iterable([input().split(', ') for _ in range(n)])
for num, prod in enumerate(sorted(sps), 1):
    print(f"{num}. {prod}")