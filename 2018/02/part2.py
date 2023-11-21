from part1 import load_data


def getBox(lines):
    for line in lines:
        for line2 in lines:
            # Remove \n on lines
            line.replace("\n", "")
            line2.replace("\n", "")

            if line == line2:
                continue
            diff = 0
            for i in range(len(line)-1):
                if line[i] != line2[i]:
                    diff += 1
            if diff == 1:
                return line, line2
    return None, None


if __name__ == '__main__':
    # Load data
    lines = load_data()

    # Get box
    box1, box2 = getBox(lines)

    # Get common letters
    common = ""
    for i in range(len(box1)):
        if box1[i] == box2[i]:
            common += box1[i]

    # Print result
    print("Box 1: " + box1)
    print("Box 2: " + box2)
    print("Common letters: " + common)
