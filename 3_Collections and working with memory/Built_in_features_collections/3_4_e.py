from itertools import chain

wants = [input().split(', ') for _ in range(3)]
products = list(chain.from_iterable(wants))
products.sort()
for num, product in enumerate(products, 1):
    print(f"{num}. {product}")
