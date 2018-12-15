# This program adds loot to an inventory. 

inv = {'gold coin': 42, 'rope': 1} # Existing inventory. 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] # Loot.

# This function adds the loot to the existing inventory dictionary.
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory.get(item, 0) + 1
        else:
            inventory[item] = 1
    return inventory     
                    
# This function prints the updated inventory. 
def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal = itemTotal + v
    print("Total number of items: " + str(itemTotal))

# This code calls the function to update the inventory.
inv = addToInventory(inv, dragonLoot)
# This code calls the function to print the updated inventory.
displayInventory(inv)
