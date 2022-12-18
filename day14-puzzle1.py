from common_functions import solve
import sys

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
    len_y = max_y - min_y + 1
    grid = [["." for _ in range(len_x)] for _ in range(len_y)]
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
    # represent it as y, x
    source = (0, 500 - min_x)
    count = 0
    path = [source]
    # simulate sand falling
    curr = source
    while len(path) > 0:
        y, x = curr
        if y >= len_y or x >= len_x or x < 0:
            # flowed into abyss
            return count
        if y == len_y - 1 or grid[y + 1][x] != "#":
            curr = (y + 1, x)
            path.append(curr)
        elif x == 0 or grid[y + 1][x - 1] != "#":
            curr = (y + 1, x - 1)
            path.append(curr)
        elif x == len_x - 1 or grid[y + 1][x + 1] != "#":
            curr = (y + 1, x + 1)
            path.append(curr)
        else:
            # sand came to rest
            grid[y][x] = "#"
            count += 1
            path.pop()
            curr = path[-1]
    return -1


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
