
import inventory
def test_logic():
    d = {}
    # We look for 'p' or a renamed function 'update_inventory'
    func = getattr(inventory, 'update_inventory', inventory.p)
    func(d, 'item', 10)
    assert d['item'] == 10
