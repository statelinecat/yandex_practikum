from itertools import permutations

n = int(input())
sps_a = sorted([input() for _ in range(n)])
for sps_b in permutations(sps_a, 3):
    sps = ', '.join(sps_b)
    print(sps)

