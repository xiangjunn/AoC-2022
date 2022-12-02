from common_functions import solve

DAY = 2


def solver(data: str) -> str:
    totalscore = 0
    win = {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    shapescore = {"X": 1, "Y": 2, "Z": 3}
    for d in data.splitlines():
        opponent, ownself = d.split()
        totalscore += shapescore[ownself]
        if win[opponent] == ownself:
            # won
            totalscore += 6
        elif draw[opponent] == ownself:
            # draw
            totalscore += 3
    return totalscore


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
