from common_functions import solve

DAY = 9


def solver(data: str):
    visited = {(0, 0)}
    H = (0, 0)
    T = (0, 0)
    for line in data.splitlines():
        direction, count = line.split(" ")
        for _ in range(int(count)):
            H = move_head(H, direction)
            T = move_tail(H, T)
            visited.add(T)
    return len(visited)


def move_head(H: tuple, direction: str) -> tuple:
    hx, hy = H
    if direction == "U":
        newH = (hx, hy + 1)
    elif direction == "D":
        newH = (hx, hy - 1)
    elif direction == "L":
        newH = (hx - 1, hy)
    elif direction == "R":
        newH = (hx + 1, hy)
    return newH


def move_tail(H: tuple, T: tuple) -> tuple:
    # move the knot, given the next position of previous knot
    # consider it as movement in x-y plane, with coordinates (x, y)
    hx, hy = H
    tx, ty = T
    if hy - ty == 2:
        newT = (hx, hy - 1)
    elif hy - ty == -2:
        newT = (hx, hy + 1)
    elif hx - tx == 2:
        newT = (hx - 1, hy)
    elif hx - tx == -2:
        newT = (hx + 1, hy)
    else:
        newT = T
    return newT


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
