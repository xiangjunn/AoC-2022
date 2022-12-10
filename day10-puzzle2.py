from common_functions import solve

DAY = 10


def solver(data: str):
    lines = data.splitlines()
    x = 1
    cycle = 1
    result = []
    for line in lines:
        if x <= cycle % 40 <= x + 2:
            result.append("#")
        else:
            result.append(".")
        if line.startswith("addx"):
            add = int(line.split()[1])
            cycle += 1
            if x <= cycle % 40 <= x + 2:
                result.append("#")
            else:
                result.append(".")
            x += add
        cycle += 1
    CRT = []
    for i in range(0, len(result), 40):
        CRT.append("".join(result[i: i + 40]))
        CRT.append("\n")
    return "".join(CRT)


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
