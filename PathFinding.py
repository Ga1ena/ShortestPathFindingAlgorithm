import random
from collections import deque


'''Map generation'''
def generate_map(m, n, land_ratio=0.3):
    total_cells = m * n  # Whole number of cells
    land_cells = int(total_cells * land_ratio)  # Number land sells
    water_cells = total_cells - land_cells  # Number water sells

    # Map filling
    cells = ['L'] * land_cells + ['W'] * water_cells  # Create 'L' и 'W' lists
    random.shuffle(cells)  # Shuffle the list
    return [cells[i * n:(i + 1) * n] for i in range(m)]  # Return a two-dimensional array m*n size


'''Cell available check'''
def is_valid_move(m, n, grid, x, y):
    return 0 <= x < m and 0 <= y < n and grid[x][y] == 'L'


'''Path finding'''
def bfs_shortest_path(grid, start, goal):
    m, n = len(grid), len(grid[0])
    queue = deque([start])  # Queue for BFS
    visited = set()  # Visited cells
    parent = {start: None}  # Path restoration

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, down, left, up

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (is_valid_move(m, n, grid, neighbor[0], neighbor[1]) and
                    neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Path restoration
    if current != goal:  # If path didn't find
        return None

    path = []
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()  # Return in the right order
    return path


def main():
    # Parameters set
    m = int(input("Enter the number of lines (M): "))
    n = int(input("Enter the number of columns (N): "))
    ax = int(input("Enter coordinate A by X: "))
    ay = int(input("Enter coordinate A by Y: "))
    bx = int(input("Enter coordinate B by X: "))
    by = int(input("Enter coordinate B by Y: "))

    # Map generation
    grid = generate_map(m, n)

    # Map output
    print("Generated map:")
    for row in grid:
        print(' '.join(row))

    # Path finding
    start = (ax, ay)
    goal = (bx, by)

    if is_valid_move(m, n, grid, ax, ay) and is_valid_move(m, n, grid, bx, by):
        path = bfs_shortest_path(grid, start, goal)
        if path:
            print("Shortest path from A to B:")
            for step in path:
                print(step)
        else:
            print("Unable to find path.")
    else:
        print("А or В is in the water.")


if __name__ == "__main__":
    main()
