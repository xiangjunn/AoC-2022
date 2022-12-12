from common_functions import solve
from collections import deque
import sys

DAY = 12


def solver(data: str):
    grid = []
    start = None
    for i, line in enumerate(data.splitlines()):
        if "S" in line:
            start = (i, line.index("S"))
        grid.append(line)

    step = bfs(grid, start)
    return step


def bfs(grid, start):
    queue = deque()
    x, y = start
    queue.append((x, y, 0))
    visited = [[False for _ in row] for row in grid]
    visited[x][y] = True
    directions = [1, 0, -1, 0, 1]
    while len(queue) > 0:
        i, j, step = queue.popleft()
        curr = grid[i][j]
        for d in range(4):
            new_i = i + directions[d]
            new_j = j + directions[d + 1]
            if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                continue
            square = grid[new_i][new_j]
            if square == "E" and curr == "z":
                # found end goal
                return step + 1
            elif grid[i][j] == "S" and square == "a":
                visited[new_i][new_j] = True
                queue.append((new_i, new_j, step + 1))
            elif not visited[new_i][new_j] and grid[i][j] != "S" and ord(square) - ord(curr) <= 1:
                visited[new_i][new_j] = True

                queue.append((new_i, new_j, step + 1))
    return sys.maxsize


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
