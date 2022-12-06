from common_functions import solve

DAY = 6


def solver(data: str) -> str:
    SIZE = 4
    for i in range(len(data) - SIZE):
        if len(set(data[i: i + SIZE])) == SIZE:
            return i + SIZE


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
