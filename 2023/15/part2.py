from collections import OrderedDict

from part1 import load_data


def get_hash(string):
    current_value = 0
    for char in string:
        # Get ASCII value
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


if __name__ == '__main__':
    # load data
    lines = load_data()
    line = lines[0].strip()

    # Split strings
    strings = line.split(',')

    # process
    boxes = {}
    for string in strings:

        # Define action to do
        if '=' in string:
            lence_label = string.split('=')[0]
            lence_value = int(string.split('=')[1])
            hash_value = get_hash(lence_label)

            # Check if the box exists
            if hash_value in boxes:
                boxes[hash_value][lence_label] = lence_value

            else:
                boxes[hash_value] = OrderedDict()
                boxes[hash_value][lence_label] = lence_value

        # Remove the lence from the box
        elif '-' in string:
            lence_label = string.split('-')[0]
            hash_value = get_hash(lence_label)
            if hash_value in boxes:
                if lence_label in boxes[hash_value]:
                    boxes[hash_value].pop(lence_label)

    # Order the boxes by key
    boxes = OrderedDict(sorted(boxes.items(), key=lambda t: t[0]))

    # Get the final value
    fianl_value = 0
    for box in boxes:
        slot = 1
        for lence in boxes[box]:
            fianl_value += (box + 1) * slot * boxes[box][lence]
            slot += 1

    print(fianl_value)