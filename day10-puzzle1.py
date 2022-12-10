from common_functions import solve

DAY = 10


def solver(data: str):
    lines = data.splitlines()
    x = 1
    cycle = 1
    strengths = 0
    for line in lines:
        if (cycle - 20) % 40 == 0:
            strengths += cycle * x
        if line.startswith("addx"):
            add = int(line.split()[1])
            cycle += 1
            if (cycle - 20) % 40 == 0:
                strengths += cycle * x
            x += add
        cycle += 1

    return strengths


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
