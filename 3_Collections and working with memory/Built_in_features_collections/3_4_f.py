from itertools import product

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
masts = ["пик", "треф", "бубен", "червей"]
masts.remove(input())
for card, mast in product(cards, masts):
    print(f"{card} {mast}")
