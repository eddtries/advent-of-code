NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBERS_STARTING_CHARS = ['e', 'f', 'n', 'o', 's', 't']
NUMBERS_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

one, two, three, four, five, six, seven, eight, nine = 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'


def load_data(path: str) -> [str]:
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.rstrip())

    return data


def part_one(path: str) -> int:
    lines = load_data(path)

    calibration_values = []

    for line in lines:
        numbers = []

        for char in line:
            if char in NUMBERS:
                numbers.append(char)

        calibration_value = numbers[0] + numbers[-1]
        calibration_values.append(int(calibration_value))

    return sum(calibration_values)


def part_two(path: str) -> int:
    lines = load_data(path)

    calibration_values = []

    for line in lines:
        numbers = []

        for char in line:
            if char not in NUMBERS_STARTING_CHARS and char not in NUMBERS:
                continue

            if char in NUMBERS:
                numbers.append(str(char))
                continue

            if char in NUMBERS_STARTING_CHARS:
                if line.startswith(one):
                    numbers.append(NUMBERS_MAP[one])
                elif line.startswith(two):
                    numbers.append(NUMBERS_MAP[two])
                elif line.startswith(three):
                    numbers.append(NUMBERS_MAP[three])
                elif line.startswith(four):
                    numbers.append(NUMBERS_MAP[four])
                elif line.startswith(five):
                    numbers.append(NUMBERS_MAP[five])
                elif line.startswith(six):
                    numbers.append(NUMBERS_MAP[six])
                elif line.startswith(seven):
                    numbers.append(NUMBERS_MAP[seven])
                elif line.startswith(eight):
                    numbers.append(NUMBERS_MAP[eight])
                elif line.startswith(nine):
                    numbers.append(NUMBERS_MAP[nine])
                else:
                    continue

        calibration_value = numbers[0] + numbers[-1]

        calibration_values.append(int(calibration_value))

    return sum(calibration_values)


if __name__ == '__main__':
    assert part_one("./pkg/y2023/data/day01.part_1.test.data") == 142
    print(part_one("./pkg/y2023/data/day01.data"))

    assert part_two("./pkg/y2023/data/day01.part_2.test.data") == 281
    print(part_two("./pkg/y2023/data/day01.data"))
