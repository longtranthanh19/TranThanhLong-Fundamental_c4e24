prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0

for fruit in prices:
    print(fruit)
    print("price:", prices[fruit])
    for st in stock:
        if fruit == st:
            print("stock:", stock[st])
            print()

            sell = prices[fruit] * stock[st]
            total += sell

print(total)