from common_functions import solve

DAY = 8

# Method 1


def solver(data: str) -> str:
    grid = list(map(lambda row: list(map(int, list(row))), data.splitlines()))
    grid_transpose = list(
        map(lambda i: list(map(lambda x: x[i], grid)), range(len(grid[0]))))
    scores = [[1 for _ in row] for row in grid]
    for i in range(len(grid)):
        calculate_scores_1d(i, grid[i], scores, True)
    for j in range(len(grid_transpose)):
        calculate_scores_1d(j, grid_transpose[j], scores, False)
    return max(max(scores, key=max))


def calculate_scores_1d(index, arr, scores, is_row):
    stack = []
    for i, height in enumerate(arr):
        while len(stack) > 0 and height >= arr[stack[-1]]:
            curr = stack.pop()
            left = search_prev_higher(curr, arr)
            right = i
            score_multiplier = (curr - left) * (right - curr)
            if is_row:
                scores[index][curr] *= score_multiplier
            else:
                scores[curr][index] *= score_multiplier
        stack.append(i)
    right = len(arr) - 1
    while len(stack) > 0:
        curr = stack.pop()
        left = search_prev_higher(curr, arr)
        score_multiplier = (curr - left) * (right - curr)
        if is_row:
            scores[index][curr] *= score_multiplier
        else:
            scores[curr][index] *= score_multiplier


def search_prev_higher(index, arr):
    for i in range(index - 1, -1, -1):
        if arr[i] >= arr[index]:
            return i
    return 0


# Method 2
"""
def solver(data: str) -> str:
    grid = list(map(lambda row: list(map(int, list(row))), data.splitlines()))
    max_score = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_score = max(max_score, calculate_score(grid, i, j))
    return max_score


def calculate_score(grid: list, i: int, j: int):
    if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
        return True
    return get_score_1d(i, j, "TOP", grid) * get_score_1d(i, j, "BOTTOM", grid)\
        * get_score_1d(i, j, "LEFT", grid) * get_score_1d(i, j, "RIGHT", grid)


def get_score_1d(i1, j1, direction, grid):
    count = 0
    if direction == "TOP":
        for x in range(i1 - 1, -1, -1):
            count += 1
            if grid[i1][j1] <= grid[x][j1]:
                break
    elif direction == "BOTTOM":
        for x in range(i1 + 1, len(grid)):
            count += 1
            if grid[i1][j1] <= grid[x][j1]:
                break
    elif direction == "LEFT":
        for y in range(j1 - 1, -1, -1):
            count += 1
            if grid[i1][j1] <= grid[i1][y]:
                break
    elif direction == "RIGHT":
        for y in range(j1 + 1, len(grid[0])):
            count += 1
            if grid[i1][j1] <= grid[i1][y]:
                break
    return count
"""

if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
