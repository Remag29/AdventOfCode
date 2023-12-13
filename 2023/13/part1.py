def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def get_boards(lines):
    boards = []
    actual_board = []
    for line in lines:
        if line == '\n':
            boards.append(actual_board)
            actual_board = []
        else:
            actual_board.append(line.strip())
    boards.append(actual_board)
    return boards


def test_mirroring(line: str, column_index: int) -> bool:
    # Get left and right
    left = line[:column_index]
    right = line[column_index:]

    # Make left and right the same size
    if len(left) > len(right):
        left = left[-len(right):]
    else:
        right = right[:len(left)]

    # Get reverse right
    reverse_right = right[::-1]

    # Test if left and reverse right are the same
    if left == reverse_right:
        return True
    else:
        return False


def get_mirror_positions(board: list) -> int:
    # Test vertical mirrors
    possible_positions = set()
    dead_positions = set()

    # Test the first line
    for column_index in range(1, len(board[0])):
        if test_mirroring(board[0], column_index):
            possible_positions.add(column_index)
        else:
            dead_positions.add(column_index)

    # Test on first line
    for line_index in range(1, len(board)):
        for column_index in possible_positions.copy():
            if column_index not in dead_positions:
                if not test_mirroring(board[line_index], column_index):
                    possible_positions.remove(column_index)
                    dead_positions.add(column_index)
    if len(possible_positions) == 1:
        return possible_positions.pop()

    return -1


def transpose_board(board: list) -> list:
    transposed_board = []
    for i in range(len(board[0])):
        transposed_board.append(''.join([board[j][i] for j in range(len(board))]))
    return transposed_board


if __name__ == '__main__':
    # load data
    lines = load_data()

    # get boards
    boards = get_boards(lines)
    print(f'Number of boards: {len(boards)}')

    # Detect mirrors positions on each board
    vertical = 0
    horizontal = 0

    for board in boards:
        # Test vertical mirrors
        mirror_positions = get_mirror_positions(board)

        # Test horizontal mirrors
        if mirror_positions == -1:
            # Transpose board
            transposed_board = transpose_board(board)

            mirror_positions = get_mirror_positions(transposed_board)
            horizontal += mirror_positions
        else:
            vertical += mirror_positions

    final_result = vertical + horizontal * 100

    print(f'Final result: {final_result}')