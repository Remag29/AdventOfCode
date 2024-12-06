from itertools import count


def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def is_on_the_map(position: tuple[int, int], lab_map: list[list[str]]) -> bool:
    # If the position is out of the map, return false
    if (position[0] < 0) or (position[1] < 0) or position[0] > len(lab_map) - 1 or position[1] > len(lab_map[0]) - 1:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Starting resolution...")

    lines = load_data()

    # Make a big map
    lab_map = []
    for line in lines:
        lab_map.append(list(line))

    print(lab_map)

    # Get the position of the gard
    for row in lab_map:
        if '^' in row:
            gard_position = (lab_map.index(row), row.index('^'))
            lab_map[gard_position[0]][gard_position[1]] = '.'  # Remove the gard beacon
    print(gard_position)

    # Start mouvement
    visited_place = set()
    mouvement_index = 0
    mouvement = [
        [-1, 0],  # Up
        [0, 1],  # Right
        [1, 0],  # Down
        [0, -1]  # Left
    ]

    while is_on_the_map(gard_position, lab_map):  # While the gard position is on the map
        visited_place.add(gard_position)  # Register gard position

        next_position = (
            gard_position[0] + mouvement[mouvement_index][0],
            gard_position[1] + mouvement[mouvement_index][1]
        )

        if not is_on_the_map(next_position, lab_map):  # Stop if the new position is out of the map
            break

        next_place_char = lab_map[next_position[0]][next_position[1]]  # Get the next place to move

        if next_place_char == '#':  # If not a way, turn right (follow the next direction in cloak wize)
            mouvement_index = (mouvement_index + 1) % 4
        else:  # if it's a way, move the gard position
            gard_position = next_position

    # Count
    result = len(visited_place)
    print(f'The result is {result}')

    # 4940 To high
    # 4939 is good, but why ??? , Can't find error in code
