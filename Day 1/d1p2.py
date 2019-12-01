sum_ = 0

with open("input.txt") as f:
    lines = f.readlines()


def recursive_fuel(fuel: int) -> int:
    if fuel == 0:
        return 0
    needed_fuel = fuel // 3 - 2
    if needed_fuel < 0:
        return 0
    return needed_fuel + recursive_fuel(needed_fuel)


for line in lines:
    try:
        line_num = int(line)
        sum_ += recursive_fuel(line_num)
    except ValueError:
        continue

print(sum_)
