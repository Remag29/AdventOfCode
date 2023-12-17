def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def is_in_board(node, board):
    x, y = node
    if x < 0 or y < 0:
        return False
    if x >= len(board) or y >= len(board[0]):
        return False
    return True


if __name__ == '__main__':
    # load data
    lines = load_data()

    board = [list(line.strip().replace('\n', '')) for line in lines]

    start = (0, 0)
    directions = ['R']
    node_to_move = [start]
    previous_seen = set()
    seen = set(start)
    seen_verticaly = set()
    seen_horizontally = set()

    while node_to_move:
        x, y = node_to_move.pop(0)
        direction = directions.pop(0)

        if board[x][y] == '.':
            if direction == 'R':
                nodes = [(x, y + 1)]
                directions_temp = ['R']
            elif direction == 'L':
                nodes = [(x, y - 1)]
                directions_temp = ['L']
            elif direction == 'U':
                nodes = [(x - 1, y)]
                directions_temp = ['U']
            elif direction == 'D':
                nodes = [(x + 1, y)]
                directions_temp = ['D']

        elif board[x][y] == '-':
            if direction == 'R':
                nodes = [(x, y + 1)]
                directions_temp = ['R']
                seen_horizontally.add((x, y))
            elif direction == 'L':
                nodes = [(x, y - 1)]
                seen_horizontally.add((x, y))
                directions_temp = ['L']
            elif direction in ['U', 'D']:
                nodes = [(x, y - 1), (x, y + 1)]
                directions_temp = ['L', 'R']
                seen_verticaly.add((x, y))

        elif board[x][y] == '|':
            if direction == 'U':
                nodes = [(x - 1, y)]
                seen_verticaly.add((x, y))
                directions_temp = ['U']
            elif direction == 'D':
                nodes = [(x + 1, y)]
                seen_verticaly.add((x, y))
                directions_temp = ['D']
            elif direction in ['R', 'L']:
                nodes = [(x - 1, y), (x + 1, y)]
                directions_temp = ['U', 'D']
                seen_horizontally.add((x, y))

        elif board[x][y] == '/':
            if direction == 'R':
                nodes = [(x - 1, y)]
                directions_temp = ['U']
            elif direction == 'L':
                nodes = [(x + 1, y)]
                directions_temp = ['D']
            elif direction == 'U':
                nodes = [(x, y + 1)]
                directions_temp = ['R']
            elif direction == 'D':
                nodes = [(x, y - 1)]
                directions_temp = ['L']

        elif board[x][y] == '\\':
            if direction == 'R':
                nodes = [(x + 1, y)]
                directions_temp = ['D']
            elif direction == 'L':
                nodes = [(x - 1, y)]
                directions_temp = ['U']
            elif direction == 'U':
                nodes = [(x, y - 1)]
                directions_temp = ['L']
            elif direction == 'D':
                nodes = [(x, y + 1)]
                directions_temp = ['R']

        # Add new nodes to move
        for i, node in enumerate(nodes):
            if is_in_board(node, board) and node not in seen_verticaly and node not in seen_horizontally:
                node_to_move.append(node)
                seen.add(node)
                directions.append(directions_temp[i])

        print(len(seen))
        if node_to_move == []:
            break

    print(len(seen))