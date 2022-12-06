from common_functions import solve

DAY = 5


def solver(data: str) -> str:
    is_procedure = False
    rows = []
    procedures = []

    for line in data.splitlines():
        if line == "":
            is_procedure = True
            continue
        if not is_procedure:
            res = list(map(lambda x: x.strip(), [
                       line[i: i + 4] for i in range(0, len(line), 4)]))
            rows.append(res)

        else:
            procedures.append(line.split())

    stacks = [[] for _ in range(len(rows[0]))]

    # create stacks
    for row in reversed(rows[:-1]):
        for i in range(len(row)):
            crate = row[i]
            if crate != "":
                stacks[i].append(crate[1])

    # change procedures to neater form.
    # index 0 - how many to move
    # index 1 - where to move from
    # index 2 - where to move to
    procedures = list(
        map(lambda p: [int(p[1]), int(p[3]) - 1, int(p[5]) - 1], procedures))
    for procedure in procedures:
        for _ in range(procedure[0]):
            stacks[procedure[2]].append(stacks[procedure[1]].pop())

    return "".join(list(map(lambda s: s.pop() if len(s) > 0 else "", stacks)))


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
