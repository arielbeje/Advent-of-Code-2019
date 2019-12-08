with open("input.txt", "r") as f:
    # Remove newline from each line
    orbit_list = [line[:-1].split(")") for line in f.readlines()]

orbit_dict = dict()


def find_parent(star: str) -> str:
    return [name for name, orbiters in orbit_dict.items()
            if star in orbiters][0]


def count_connections(star: str) -> int:
    if star == "COM":
        return 0
    return 1 + count_connections(find_parent(star))


for orbit in orbit_list:
    if orbit[0] in orbit_dict:
        orbit_dict[orbit[0]].append(orbit[1])
    else:
        orbit_dict[orbit[0]] = [orbit[1]]

    if orbit[1] not in orbit_dict:
        orbit_dict[orbit[1]] = list()

sum_ = 0
for orbit in orbit_dict:
    sum_ += count_connections(orbit)
print(sum_)
