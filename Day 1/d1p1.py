with open("input.txt") as f:
    lines = f.readlines()

sum_ = 0

for line in lines:
    try:
        line_num = int(line)
        sum_ += line_num // 3 - 2
    except ValueError:
        break

print(sum_)
