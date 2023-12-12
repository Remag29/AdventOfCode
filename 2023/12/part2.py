from functools import cache

from part1 import load_data


def read_line(line):
    # read line
    line = line.strip()
    placement = line.split(' ')[0]
    numbers = line.split(' ')[1].split(',')
    numbers = [int(number) for number in numbers]

    # upgrade for part2
    fold_times = 5
    new_placement = placement
    new_numbers = numbers.copy()
    for _ in range(fold_times - 1):
        new_placement += '?' + placement
        new_numbers += numbers

    return new_placement, new_numbers


@cache
def count_possible_position(placement: str, numbers: tuple[int, ...]) -> int:
    # Base case
    if not numbers:
        # is everything left in springs either unknown or not a spring
        if all(char in [".", "?"] for char in placement):
            return 1
        return 0

    group1_size = numbers[0]
    remaining_groups = numbers[1:]

    # Remaining spaces is the number of spaces left in the springs
    remaining_spaces = sum(remaining_groups) + len(remaining_groups)

    count = 0
    # Try all possible positions for the first group
    for i in range(len(placement) - remaining_spaces - group1_size + 1):
        possible_springs = "." * i + "#" * group1_size + "."

        # Check if the possible springs are valid
        if all(spring == possible_spring or spring == "?" for spring, possible_spring in zip(placement, possible_springs)):
            # Recursively count the number of possible positions for the remaining groups
            count += count_possible_position(placement[len(possible_springs):], remaining_groups)

    return count


if __name__ == '__main__':
    # laod data
    lines = load_data()

    final_result = 0

    for line in lines:
        placement, numbers = read_line(line)
        final_result += count_possible_position(placement, tuple(numbers))

    print(final_result)
