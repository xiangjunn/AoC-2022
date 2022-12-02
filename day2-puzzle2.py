from common_functions import solve

DAY = 2


def solver(data: str) -> str:
    totalscore = 0
    win = {"A": "B", "B": "C", "C": "A"}
    lose = {"A": "C", "B": "A", "C": "B"}
    shapescore = {"A": 1, "B": 2, "C": 3}
    for d in data.splitlines():
        opponent, outcome = d.split()
        if outcome == "X":
            # lose
            shapetochoose = lose[opponent]
        elif outcome == "Y":
            # draw, so same shape as opponent
            totalscore += 3
            shapetochoose = opponent
        else:
            # win
            totalscore += 6
            shapetochoose = win[opponent]

        totalscore += shapescore[shapetochoose]

    return totalscore


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
