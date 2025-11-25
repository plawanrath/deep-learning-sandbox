
def update_inventory(inventory: dict[str, int], item: str, quantity: int) -> dict[str, int]:
    """Add the given quantity of an item to the inventory in place."""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory


def get_total_quantity(inventory: dict[str, int]) -> int:
    """Return the total count of all items in the inventory."""
    total = 0
    for item_name in inventory:
        total += inventory[item_name]
    return total


# Backwards compatibility aliases
add_item = update_inventory
p = update_inventory
count_items = get_total_quantity
get_total = get_total_quantity
c = get_total_quantity
