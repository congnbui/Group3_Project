##(a) 35
##(b) 4
##(c) True
##(d)Error
##(e)0
##(f)['apples', 'bananas', 'grapes', 'oranges']
##(g) False


def add_fruit(inventory, fruit, quantity=0):
    """ add a number of fruits to the inventory """
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return inventory

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)

