from common_functions import solve

DAY = 1


def solver(data: str) -> str:
    return max(list(map(lambda x: sum(list(map(lambda y: 0 if y == "" else int(y), x.split("\n")))), data.split("\n\n"))))


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
