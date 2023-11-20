def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    # load data
    board = load_data()

    # Set the starting position
    position_x = 0
    position_y = 0

    # Set the move
    move = [3, 1]

    # Get the last position of each axis
    lasty = len(board)
    lastx = len(board[0]) - 1 # -1 because of the \n, there is just 31 characters not 32

    trees = 0

    # Move the toboggan and count the trees until the last position
    while position_y < lasty:
        position_x = (position_x + move[0]) % lastx
        position_y = position_y + move[1]

        if position_y >= lasty:
            break

        if board[position_y][position_x] == '#':
            trees += 1

    print("The toboggan hit", trees, "trees")
