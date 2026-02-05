"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    count = dict()
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
    pass


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    new_item_count = create_inventory(items)
    for key in new_item_count:
        if key not in inventory:
            inventory[key] = new_item_count[key]
        else:
            inventory[key] += new_item_count[key]
    return inventory
    pass


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    quest_items = create_inventory(items)
    for item in quest_items:
        if item in inventory:
            if inventory[item] - quest_items[item] > 0:
                inventory[item] -= quest_items[item]
            else:
                inventory[item] = 0
        else:    
            continue
    return inventory
    pass


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory
    pass


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            tuples = (key,inventory[key])
            inventory_list.append(tuples)
        else:
            continue
    return inventory_list
    pass

