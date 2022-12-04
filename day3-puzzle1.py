from common_functions import solve

DAY = 3


def solver(data: str) -> str:
    small_a = ord("a")
    big_a = ord("A")
    total = 0
    for line in data.splitlines():
        mid = len(line) // 2
        first = set(line[:mid])
        second = set(line[mid:])
        common = (first & second).pop()
        if common.isupper():
            priority = ord(common) - big_a + 27
        else:
            priority = ord(common) - small_a + 1
        total += priority
    return total


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
