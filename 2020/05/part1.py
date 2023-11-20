def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def calculate_place(line):
    # Split letters in 7 and 3
    row = line[:7]
    col = line[7:]

    # Max
    max_row = 127
    max_col = 7

    # Min
    min_row = 0
    min_col = 0

    # Calculate row
    for letter in row:
        if letter == 'F':
            max_row = (max_row + min_row) // 2
        else:
            min_row = (max_row + min_row) // 2 + 1

    # Calculate col
    for letter in col:
        if letter == 'L':
            max_col = (max_col + min_col) // 2
        else:
            min_col = (max_col + min_col) // 2 + 1

    # Calculate place
    place = max_row * 8 + max_col

    return place


if __name__ == '__main__':
    # load data
    lines = load_data()

    # Get the places
    places = []
    for line in lines:
        places.append(calculate_place(line))

    # Get the max place
    max_place = max(places)
    print(max_place)
