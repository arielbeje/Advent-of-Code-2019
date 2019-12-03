with open("input.txt") as f:
    file_lines = [line.replace("\n", "") for line in f.readlines()]

points_crossed = [[(0, 0)], [(0, 0)]]


def manhatten_distance(point) -> int:
    return abs(point[0]) + abs(point[1])


for i, line in enumerate(file_lines):
    current_point = [0, 0]
    for instruction in line.split(","):
        length = int(instruction[1:])
        if instruction.startswith("R"):
            for _ in range(length):
                current_point[0] += 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("L"):
            for _ in range(length):
                current_point[0] -= 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("U"):
            for _ in range(length):
                current_point[1] += 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("D"):
            for _ in range(length):
                current_point[1] -= 1
                points_crossed[i].append(tuple(current_point))
        else:
            print("Something went wrong")
            continue

crossing_points_set = set(points_crossed[0])
crossing_points = list(crossing_points_set.intersection(set(
    points_crossed[1])))
# distnaces = [manhatten_distance(j) for j in crossing_points]
# crossing_points.sort(key = lambda x: manhatten_distance(x))
distances = [manhatten_distance(x) for x in crossing_points]
# zipped_pairs = zip(distances, crossing_points)
# print([x for _, x in sorted(zipped_pairs)])
print(sorted(distances))
