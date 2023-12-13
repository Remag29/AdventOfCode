from part1 import load_data, get_boards, transpose_board, test_mirroring, get_mirror_positions


def get_mirror_positions_with_smudge(board: list) -> int:
    # Get the previous mirror position (without smudge)
    original_place = get_mirror_positions(board)

    # Test all possible smudges positions
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Copy the board
            board_copy = board.copy()

            # Change the symbol (possible smudge)
            if board[i][j] == '#':
                board_copy[i] = board[i][:j] + '.' + board[i][j + 1:]
            else:
                board_copy[i] = board[i][:j] + '#' + board[i][j + 1:]

            # Test mirroring on this modified board
            # Test vertical mirrors
            possible_positions = set()
            dead_positions = set()

            # Test the first line
            for column_index in range(1, len(board_copy[0])):
                if test_mirroring(board_copy[0], column_index):
                    possible_positions.add(column_index)
                else:
                    dead_positions.add(column_index)

            # Test on first line
            for line_index in range(1, len(board_copy)):
                for column_index in possible_positions.copy():
                    if column_index not in dead_positions:
                        if not test_mirroring(board_copy[line_index], column_index):
                            possible_positions.remove(column_index)
                            dead_positions.add(column_index)

            # Verify if is there a new different position for the mirror
            if len(possible_positions) == 1:
                value = possible_positions.pop()
                if value != original_place:
                    # New !
                    return value
            elif len(possible_positions) == 2:
                value = possible_positions.pop()
                if value != original_place:
                    # New !
                    return value
                else:
                    # Not new so return the other one
                    return possible_positions.pop()
    return -1


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
        mirror_positions = get_mirror_positions_with_smudge(board)

        # Test horizontal mirrors
        if mirror_positions == -1:
            # Transpose board
            transposed_board = transpose_board(board)

            # Test horizontal mirrors
            mirror_positions = get_mirror_positions_with_smudge(transposed_board)
            horizontal += mirror_positions
        else:
            vertical += mirror_positions

    final_result = vertical + horizontal * 100

    print(f'Final result: {final_result}')
