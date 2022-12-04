from common_functions import solve

DAY = 3


def solver(data: str) -> str:
    GROUPSIZE = 3
    intersection = None
    total = 0
    for i, line in enumerate(data.splitlines()):
        if i % GROUPSIZE == 0:
            intersection = set(line)
        else:
            intersection &= set(line)
            if i % GROUPSIZE == GROUPSIZE - 1:
                common = intersection.pop()
                total += get_priority(common)
    return total


def get_priority(letter: str) -> int:
    small_a = ord("a")
    big_a = ord("A")
    if letter.isupper():
        priority = ord(letter) - big_a + 27
    else:
        priority = ord(letter) - small_a + 1
    return priority


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
