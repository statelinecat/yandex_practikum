from itertools import chain, permutations

num = int(input())
sps = sorted(chain.from_iterable(input().split(", ") for _ in range(num)))
for sps_b in permutations(sps, 3):
    print(" ".join(sps_b))

goods_iter = chain.from_iterable(input().split(", ") for _ in range(int(input())))
for values in permutations(sorted(goods_iter), 3):
    print(" ".join(values))