from common_functions import solve

DAY = 4


def solver(data: str) -> str:
    count = 0
    for line in data.splitlines():
        range1, range2 = list(
            map(lambda r: tuple(map(int, r.split("-"))), line.split(",")))
        if is_contained(range1, range2) or is_contained(range2, range1):
            count += 1
    return count


def is_contained(range1, range2):
    """
    Returns true if range1 fully contains range2, else false
    """
    start1, end1 = range1
    start2, end2 = range2
    return start1 <= start2 and end1 >= end2


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
