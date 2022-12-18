from common_functions import solve

DAY = 15


def solver(data: str):
    sensors = []
    beacons = []
    for line in data.splitlines():
        sensor, beacon = line.split(":")
        sensor = extract_info(sensor)
        beacon = extract_info(beacon)
        sensors.append(sensor)
        beacons.append(beacon)

    max_range = 4_000_000

    for row in range(max_range + 1):
        not_possible = []
        for i in range(len(sensors)):
            sensor = sensors[i]
            beacon = beacons[i]
            dist = get_manhattan_dist(
                sensor[0], sensor[1], beacon[0], beacon[1])
            vert_dist_to_rownum = abs(sensor[1] - row)
            if vert_dist_to_rownum <= dist:
                curr_x = sensor[0]
                leftover = dist - vert_dist_to_rownum
                not_possible.append(
                    [max(0, curr_x - leftover), min(curr_x + leftover, max_range)])
        not_possible = merge_interval(not_possible)
        if len(not_possible) != 1:
            # since there is only 1 position, the length must be 2
            end1 = not_possible[0][1]
            start2 = not_possible[1][0]
            x = end1 + (start2 - end1) // 2
            return (x * 4_000000) + row
    return -1


def extract_info(s: str):
    info = s.split("=")
    y = int(info[2])
    x = int(info[1].split(",")[0])
    return (x, y)


def get_manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def merge_interval(arr):
    # modified merge interval such that it also merge when the difference is 1
    arr.sort()
    res = []
    curr = arr[0]
    for i in range(1, len(arr)):
        start, end = arr[i]
        if start <= curr[1] + 1:
            curr[1] = max(curr[1], end)
        else:
            res.append(curr)
            curr = arr[i]
    res.append(curr)
    return res


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
