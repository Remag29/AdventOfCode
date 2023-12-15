def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    # load data
    lines = load_data()
    line = lines[0].strip()

    # Split strings
    strings = line.split(',')

    fianl_value = 0
    for string in strings:
        current_value = 0
        for char in string:
            # Get ASCII value
            current_value = ((current_value + ord(char)) * 17) % 256
        fianl_value += current_value

    print(fianl_value)
