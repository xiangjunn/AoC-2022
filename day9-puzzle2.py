from common_functions import solve

DAY = 9


def solver(data: str):
    visited = {(0, 0)}
    # index 0 represents the head, the rest represent the 9 tails
    positions = [(0, 0) for i in range(10)]
    for line in data.splitlines():
        direction, count = line.split(" ")
        for _ in range(int(count)):
            positions[0] = move_head(positions[0], direction)
            for i in range(1, len(positions)):
                positions[i] = move_tail(positions[i - 1], positions[i])
                if i == 9:
                    visited.add(positions[i])
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
    move_x = (tx - hx) // 2 if tx - hx >= 0 else -((hx - tx) // 2)
    move_y = (ty - hy) // 2 if ty - hy >= 0 else -((hy - ty) // 2)
    if hy - ty == 2:
        newT = (hx + move_x, hy - 1)
    elif hy - ty == -2:
        newT = (hx + move_x, hy + 1)
    elif hx - tx == 2:
        newT = (hx - 1, hy + move_y)
    elif hx - tx == -2:
        newT = (hx + 1, hy + move_y)
    else:
        newT = T
    return newT


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
