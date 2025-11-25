
def find_shortest_path(grid, start, end):
    # grid: 2D list, 0=empty, 1=wall
    # Return list of tuples [(r,c), ...] or None
    # TODO: Implement A* or BFS
    if not grid or not grid[0]:
        return None

    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end

    # Reject out-of-bounds or blocked endpoints early
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    if not (in_bounds(sr, sc) and in_bounds(er, ec)):
        return None
    if grid[sr][sc] == 1 or grid[er][ec] == 1:
        return None

    # Standard BFS over 4-neighborhood to ensure a shortest path.
    from collections import deque

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])
    prev = {start: None}

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            break
        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or grid[nr][nc] == 1:
                continue
            if (nr, nc) in prev:
                continue
            prev[(nr, nc)] = (r, c)
            queue.append((nr, nc))

    if end not in prev:
        return None

    # Reconstruct path from end to start.
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path
