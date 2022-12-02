from common_functions import solve
import heapq

DAY = 1


def solver(data: str) -> str:
    # store the negative of sum so that can make it a "maxheap"
    calories = list(map(lambda x: -sum(list(map(lambda y: 0 if y ==
                    "" else int(y), x.split("\n")))), data.split("\n\n")))
    heapq.heapify(calories)
    total_calories_top_3 = 0
    for _ in range(3):
        # since we store the sum as negative, should change it to positive first
        total_calories_top_3 -= heapq.heappop(calories)

    return total_calories_top_3


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
