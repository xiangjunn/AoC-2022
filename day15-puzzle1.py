from common_functions import solve

DAY = 15


def solver(data: str):
    sensors = []
    beacons = []
    row_num = 2_000_000
    # beacons that are in same row as row_num value
    beacons_same = set()
    for line in data.splitlines():
        sensor, beacon = line.split(":")
        sensor = extract_info(sensor)
        beacon = extract_info(beacon)
        if beacon[1] == row_num:
            beacons_same.add(beacon)
        sensors.append(sensor)
        beacons.append(beacon)

    not_possible = []
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        dist = get_manhattan_dist(sensor[0], sensor[1], beacon[0], beacon[1])
        vert_dist_to_rownum = abs(sensor[1] - row_num)
        if vert_dist_to_rownum <= dist:
            curr_x = sensor[0]
            leftover = dist - vert_dist_to_rownum
            not_possible.append([curr_x - leftover, curr_x + leftover])
    not_possible = merge_interval(not_possible)
    total = 0
    for interval in not_possible:
        count = interval[1] - interval[0] + 1
        for b in beacons_same:
            if interval[0] <= b[1] <= interval[1]:
                count -= 1
        total += count

    return total


def extract_info(s: str):
    info = s.split("=")
    y = int(info[2])
    x = int(info[1].split(",")[0])
    return (x, y)


def get_manhattan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def merge_interval(arr):
    arr.sort()
    res = []
    curr = arr[0]
    for i in range(1, len(arr)):
        start, end = arr[i]
        if start <= curr[1]:
            curr[1] = max(curr[1], end)
        else:
            res.append(curr)
            curr = arr[i]
    res.append(curr)
    return res


if __name__ == "__main__":
    output = solve(DAY, solver)
    print(output)
