with open("input.txt") as f:
    numbers = [int(x) for x in f.read().split("\n")[0].split(",")]
i = 0

while numbers[i] != 99:
    instruction = numbers[i] % 100
    # print(instruction)
    if instruction == 1 or instruction == 2:
        parameter_modes = (numbers[i] // 100 % 10, numbers[i] // 1000)
        params = []
        for index, mode in enumerate(parameter_modes):
            params.append(numbers[i + index +
                                  1] if mode == 1 else numbers[numbers[i +
                                                                       index +
                                                                       1]])
        params.append(numbers[i + 3])
        if instruction == 1:
            numbers[params[2]] = params[0] + params[1]
        elif instruction == 2:
            numbers[params[2]] = params[0] * params[1]
        i += 4
    elif instruction == 3:
        numbers[numbers[i + 1]] = int(input())
        i += 2
    elif instruction == 4:
        print(numbers[numbers[i + 1]])
        i += 2
    else:
        print("Something went wrong")
        print(f"i = {i}")
        print(f"numbers[i] = {numbers[i]}")
        break
