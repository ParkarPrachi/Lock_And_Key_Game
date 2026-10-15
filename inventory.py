def take_item(item_name, current_room):
    global score
    items = rooms[current_room]['items']
    if item_name not in items:
        print("That item is not in this room.")
    elif len(inventory) >= 3:
        print("Inventory full. You can only carry 3 items.")
    elif item_name in inventory:
        print("You already have that item in your inventory.")
    else:
        inventory.append(item_name)
        items.remove(item_name)
        print("You collected the " + item_name + ".")

def drop_item(item_name, current_room):
    if item_name not in inventory:
        print("You don't have that item in your inventory.")
    else:
        inventory.remove(item_name)
        rooms[current_room]['items'].append(item_name)
        print("You dropped the " + item_name + ".")

def show_inventory():
    if inventory:
        print("Inventory: " + ", ".join(inventory))
    else:
        print("Inventory is empty.")

def inspect_item(item_name):
    if item_name in inventory:
        print("You are carrying the " + item_name + ".")
    else:
        print("You don't have that item in your inventory.")