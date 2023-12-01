NUMBERS = [str(x) for x in range(1, 10)]
NUMBERS_STARTING_CHARS = ["e", "f", "n", "o", "s", "t"]


def load_data(path: str) -> [str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.rstrip())

    return data


def part_one(path: str) -> int:
    data = load_data(path)

    calibration_values = []

    for string in data:
        numbers = []

        for char in string:
            if char in NUMBERS:
                numbers.append(char)

        calibration_value = numbers[0] + numbers[-1]
        calibration_values.append(calibration_value)

    return sum([int(x) for x in calibration_values])


def part_two(path: str) -> int:
    data = load_data(path)

    calibration_values = []

    for string in data:
        numbers = []

        while True:
            if len(string) <= 0:
                break

            char = string[0]

            if char not in NUMBERS_STARTING_CHARS and char not in NUMBERS:
                string = string[1:]
                continue

            if char in NUMBERS:
                numbers.append(char)
                string = string[1:]
                continue

            if char in NUMBERS_STARTING_CHARS:
                if string.startswith("one"):
                    numbers.append(1)
                    string = string[1:]
                elif string.startswith("two"):
                    numbers.append(2)
                    string = string[1:]
                elif string.startswith("three"):
                    numbers.append(3)
                    string = string[1:]
                elif string.startswith("four"):
                    numbers.append(4)
                    string = string[1:]
                elif string.startswith("five"):
                    numbers.append(5)
                    string = string[1:]
                elif string.startswith("six"):
                    numbers.append(6)
                    string = string[1:]
                elif string.startswith("seven"):
                    numbers.append(7)
                    string = string[1:]
                elif string.startswith("eight"):
                    numbers.append(8)
                    string = string[1:]
                elif string.startswith("nine"):
                    numbers.append(9)
                    string = string[1:]
                else:
                    string = string[1:]

        if len(numbers) == 1:
            calibration_value = str(numbers[0]) + str(numbers[0])
        else:
            calibration_value = str(numbers[0]) + str(numbers[-1])

        calibration_values.append(calibration_value)

    for i, calibration_value in enumerate(calibration_values):
        print(f'{i+1}: {calibration_value}')

    return sum([int(x) for x in calibration_values])


if __name__ == '__main__':
    assert part_one(
        "./python_solutions/y2023/data/day01.part_1.test.data") == 142
    print(part_one("./python_solutions/y2023/data/day01.data"))

    assert part_two(
        "./python_solutions/y2023/data/day01.part_2.test.data") == 281
    print(part_two("./python_solutions/y2023/data/day01.data"))
