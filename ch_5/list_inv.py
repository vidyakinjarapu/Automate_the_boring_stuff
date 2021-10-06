'''
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
'''


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        if item in inventory:
            inventory[item] += 1
        # if item in inventory:
        #     inventory[item] += 1
        # else:
        #     inventory[item] = 1
    return inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)
