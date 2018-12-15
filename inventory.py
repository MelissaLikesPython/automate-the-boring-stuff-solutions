# This program lists your inventory for a game.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print(v, k)
        itemTotal = itemTotal + v
    print("Total number of items: " + str(itemTotal))

displayInventory(stuff)    
