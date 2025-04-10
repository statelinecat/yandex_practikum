from itertools import combinations

players = [input() for _ in range(int(input()))]
for player1, player2 in combinations(players, 2):
    print(f'{player1} - {player2}')

