from itertools import cycle, islice

porridges = [input() for _ in range(int(input()))]
days = int(input())
for porridge in islice(cycle(porridges), 0, days):
    print(porridge)