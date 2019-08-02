#   defining the inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42,
         'dagger': 1, 'arrow': 12}
dragoon_loot = ['gold coin', 'dagger', 'gold coin', 'ruby',
                'gold coin', 'ruby', 'dagger', 'diamond']


def display_inventory(inventory):
    print("inventory")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('updated stuff', stuff)
    print('total no of items: ' + str(item_total))


def add_to_dictionary(inventory, added_items):
    print("Last inventory", inventory)

    for count in added_items:
        for k, v in inventory.items():
            if count == k:
                inventory[k] = inventory.get(k, 0) + 1
        if count not in inventory:
            inventory.update({count: inventory.get(count, 0) + 1})
    display_inventory(inventory)


add_to_dictionary(stuff, dragoon_loot)
