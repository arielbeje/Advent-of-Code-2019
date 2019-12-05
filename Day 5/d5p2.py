with open("input.txt") as f:
    numbers = [int(x) for x in f.read().split("\n")[0].split(",")]
i = 0

while numbers[i] != 99:
    instruction = numbers[i] % 100
    if 0 < instruction < 9:
        if instruction < 3 or instruction > 6:
            parameter_modes = (numbers[i] // 100 % 10, numbers[i] // 1000)
            params = []
            for index, mode in enumerate(parameter_modes):
                params.append(numbers[i + index + 1] if mode ==
                              1 else numbers[numbers[i + index + 1]])
            params.append(numbers[i + 3])

            if instruction == 1:
                numbers[params[2]] = params[0] + params[1]
            elif instruction == 2:
                numbers[params[2]] = params[0] * params[1]

            elif instruction == 7:
                if params[0] < params[1]:
                    numbers[params[2]] = 1
                else:
                    numbers[params[2]] = 0
            elif instruction == 8:
                if params[0] == params[1]:
                    numbers[params[2]] = 1
                else:
                    numbers[params[2]] = 0
            i += 4

        elif instruction < 5:
            if instruction == 3:
                numbers[numbers[i + 1]] = int(input())
            elif instruction == 4:
                print(numbers[numbers[i + 1]])
            i += 2

        else:
            parameter_modes = (numbers[i] // 100 % 10, numbers[i] // 1000)
            params = []
            for index, mode in enumerate(parameter_modes):
                params.append(numbers[i + index + 1] if mode ==
                              1 else numbers[numbers[i + index + 1]])

            if instruction == 5:
                if params[0] != 0:
                    i = params[1]
                else:
                    i += 3
            elif instruction == 6:
                if params[0] == 0:
                    i = params[1]
                else:
                    i += 3

    else:
        print("Something went wrong")
        print(f"i = {i}")
        print(f"numbers[i] = {numbers[i]}")
        break
