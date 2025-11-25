
import pytest
import inventory

def test_workflow():
    # Check if logic is preserved after refactoring
    # We assume the agent keeps the function names or we might need to update imports
    # Ideally, the agent should rename functions to 'process_inventory' etc.
    # For this test, we might need to inspect the module attributes if names change,
    # but let's assume for now strict API preservation OR intelligent alias.

    # Setup
    inv = {}

    # If functions were renamed, we try to find them, otherwise use originals
    add_func = getattr(inventory, 'add_item', None) or getattr(inventory, 'update_inventory', None) or inventory.p
    count_func = getattr(inventory, 'get_total', None) or getattr(inventory, 'count_items', None) or inventory.c

    add_func(inv, 'apple', 10)
    add_func(inv, 'banana', 5)
    add_func(inv, 'apple', 2)

    assert inv['apple'] == 12
    assert count_func(inv) == 17
