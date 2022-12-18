from common_functions import solve
import sys
from collections import deque

DAY = 14


def solver(data: str):
    min_x = sys.maxsize
    min_y = 0
    max_x = - sys.maxsize
    max_y = - sys.maxsize
    rocks = []
    for line in data.splitlines():
        curr_rocks = []
        pairs = line.split(" -> ")
        for pair in pairs:
            x, y = list(map(int, pair.split(",")))
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            curr_rocks.append((x, y))
        rocks.append(curr_rocks)
    # normalize
    rocks = list(map(lambda x: list(
        map(lambda y: (y[0] - min_x, y[1] - min_y), x)), rocks))
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 3
    grid = [deque("." for _ in range(len_x)) for _ in range(len_y)]
    for rock in rocks:
        for i in range(1, len(rock)):
            first_x, first_y = rock[i - 1]
            second_x, second_y = rock[i]
            if first_x == second_x:
                # vertical
                for j in range(min(first_y, second_y), max(first_y, second_y) + 1):
                    grid[j][first_x] = "#"
            else:
                # horizontal
                for j in range(min(first_x, second_x), max(first_x, second_x) + 1):
                    grid[first_y][j] = "#"
    for i in range(len(grid[0])):
        grid[len(grid) - 1][i] = "#"
    # represent it as y, x
    source = (0, 500 - min_x)
    count = 0
    path = [source]
    # simulate sand falling
    curr = source
    offset = 0
    while len(path) > 0:
        y, x = curr
        if x + offset >= len_x:
            len_x += 1
            for i, y_row in enumerate(grid):
                if i == len(grid) - 1:
                    y_row.append("#")
                else:
                    y_row.append(".")
        elif x + offset < 0:
            offset += 1
            len_x += 1
            for i, y_row in enumerate(grid):
                if i == len(grid) - 1:
                    y_row.appendleft("#")
                else:
                    y_row.appendleft(".")
        if grid[y + 1][x + offset] != "#" and y < len_y - 2:
            curr = (y + 1, x)
            path.append(curr)
        elif (x + offset == 0 or grid[y + 1][x - 1 + offset] != "#") and y < len_y - 2:
            curr = (y + 1, x - 1)
            path.append(curr)
        elif (x + offset == len_x - 1 or grid[y + 1][x + 1 + offset] != "#") and y < len_y - 2:
            curr = (y + 1, x + 1)
            path.append(curr)
        else:
            # sand came to rest
            grid[y][x + offset] = "#"
            count += 1
            if y == source[0] and x == source[1]:
                # it gets stuck at source
                return count
            path.pop()
            curr = path[-1]
    return -1


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
