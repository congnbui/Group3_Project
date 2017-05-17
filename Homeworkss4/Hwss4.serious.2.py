prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

purchased_items = {
    "banana": 5,
    "orange": 3
    }

total = 0

for item, number in purchased_items.items():
    print("{0}, quantity: {1}, unit price: {2}, cost: {3}".format(item, number, prices[item], number*prices[item]))
    total += number*prices[item]

print("total cost = ", total)
