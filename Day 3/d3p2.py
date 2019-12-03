with open("input.txt") as f:
    file_lines = [line.replace("\n", "") for line in f.readlines()]

points_crossed = [[(0, 0, 0)], [(0, 0, 0)]]

for i, line in enumerate(file_lines):
    current_point = [0, 0, 0]
    for instruction in line.split(","):
        length = int(instruction[1:])
        if instruction.startswith("R"):
            for _ in range(length):
                current_point[0] += 1
                current_point[2] += 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("L"):
            for _ in range(length):
                current_point[0] -= 1
                current_point[2] += 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("U"):
            for _ in range(length):
                current_point[1] += 1
                current_point[2] += 1
                points_crossed[i].append(tuple(current_point))
        elif instruction.startswith("D"):
            for _ in range(length):
                current_point[1] -= 1
                current_point[2] += 1
                points_crossed[i].append(tuple(current_point))
        else:
            print("Something went wrong")
            continue

# line1_crossed_points = set(points_crossed[0])
points_crossed_pure = [[(x[0], x[1]) for x in points_crossed[0]],
                       [(x[0], x[1]) for x in points_crossed[1]]]
crossing_points_set = set(points_crossed_pure[0])
crossing_points = list(
    crossing_points_set.intersection(set(points_crossed_pure[1])))

steps = []
for point in crossing_points:
    steps.append(points_crossed[0][points_crossed_pure[0].index(point)][2] +
                 points_crossed[1][points_crossed_pure[1].index(point)][2])
steps.sort()
# zipped_pairs = zip(steps, crossing_points)
# print([x for _, x in sorted(zipped_pairs)])
# print(points_crossed)
# print(crossing_points)
print(steps)
