from common_functions import solve
import json
from functools import cmp_to_key

DAY = 13


def solver(data: str):
    lines = data.splitlines()
    result = []
    for i in range(0, len(lines), 3):
        first = json.loads(lines[i])
        second = json.loads(lines[i + 1])
        result.append(first)
        result.append(second)
    result.append([[2]])
    result.append([[6]])
    result.sort(key=cmp_to_key(checkorder), reverse=True)
    return (result.index([[2]]) + 1) * (result.index([[6]]) + 1)


def checkorder(first, second):
    if type(first) == list and type(second) == list:
        if len(first) == 0 and len(second) == 0:
            return 0
        for i in range(len(first)):
            if i >= len(second):
                return -1
            result = checkorder(first[i], second[i])
            if result == 1:
                return 1
            elif result == -1:
                return -1
        return len(first) < len(second)

    elif type(first) == list:
        return checkorder(first, [second])
    elif type(second) == list:
        return checkorder([first], second)
    else:
        if first < second:
            return 1
        elif first > second:
            return -1
        else:
            return 0


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
