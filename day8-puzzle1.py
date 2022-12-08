from common_functions import solve

DAY = 8


def solver(data: str) -> str:
    grid = list(map(lambda row: list(map(int, list(row))), data.splitlines()))
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_visible(grid, i, j):
                count += 1
    return count


def is_visible(grid: list, i: int, j: int):
    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
        return True
    return is_taller(i, j, "TOP", grid) or is_taller(i, j, "BOTTOM", grid)\
        or is_taller(i, j, "LEFT", grid) or is_taller(i, j, "RIGHT", grid)


def is_taller(i1, j1, direction, grid):
    if direction == "TOP":
        for x in range(0, i1):
            if grid[i1][j1] <= grid[x][j1]:
                return False
    if direction == "BOTTOM":
        for x in range(i1 + 1, len(grid)):
            if grid[i1][j1] <= grid[x][j1]:
                return False
    if direction == "LEFT":
        for y in range(0, j1):
            if grid[i1][j1] <= grid[i1][y]:
                return False
    if direction == "RIGHT":
        for y in range(j1 + 1, len(grid[0])):
            if grid[i1][j1] <= grid[i1][y]:
                return False
    return True


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
