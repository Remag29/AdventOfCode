def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def test_evolution(report: list[int]) -> bool:
    # test if the report's number an ascending or descending
    return report == sorted(report) or report == sorted(report, reverse=True)


def test_adjacent_level(report: list[int]) -> bool:
    # Test if to adjacent number differ by at least one and at most three
    for number_index in range(len(report) - 1):
        if abs(report[number_index] - report[number_index + 1]) > 3 or abs(
                report[number_index] - report[number_index + 1]) < 1:
            return False

    return True


if __name__ == '__main__':
    print("Starting resolution...")

    # Load lines
    lines = load_data()

    # Check each line/report
    safe_reports = 0

    for line in lines:
        report = [int(x) for x in line.split(' ')]

        if test_evolution(report) and test_adjacent_level(report):
            safe_reports += 1

    print(f'{safe_reports} reports are safe.')
