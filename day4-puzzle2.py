from common_functions import solve

DAY = 4


def solver(data: str) -> str:
    count = 0
    for line in data.splitlines():
        range1, range2 = list(
            map(lambda r: tuple(map(int, r.split("-"))), line.split(",")))
        if has_overlap(range1, range2):
            count += 1
    return count


def has_overlap(range1, range2):
    """
    Returns true if there is an overlap, else false
    """
    start1, end1 = range1
    start2, end2 = range2
    return (start1 <= start2 <= end1) or (start1 <= end2 <= end1) or (start2 < start1 and end2 > end1)


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
