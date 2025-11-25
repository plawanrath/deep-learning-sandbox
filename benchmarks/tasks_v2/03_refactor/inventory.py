
"""Utility functions for managing a simple in-memory inventory."""

from typing import Dict


def update_inventory(inventory: Dict[str, int], item: str, quantity: int) -> Dict[str, int]:
    """Add ``quantity`` to the count for ``item`` in ``inventory`` and return the dict."""
    current_quantity = inventory.get(item, 0)
    inventory[item] = current_quantity + quantity
    return inventory


# Backwards compatibility with the old, poorly named helper.
p = update_inventory
