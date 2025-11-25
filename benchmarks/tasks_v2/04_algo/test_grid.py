
from grid_search import find_shortest_path
def test_simple_path():
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    path = find_shortest_path(grid, (0,0), (2,2))
    assert path is not None
    # Shortest walk is right, right, down, down -> 5 coordinates including endpoints
    assert len(path) == 5
def test_no_path():
    grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert find_shortest_path(grid, (0,0), (0,2)) is None
