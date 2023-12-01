def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def readLine(line):
    line.replace('\n', '')
    line = line.split(' ')
    id = line[0][1:]
    x = line[2].split(',')[0]
    y = line[2].split(',')[1][:-1]
    w = line[3].split('x')[0]
    h = line[3].split('x')[1]

    return id, x, y, w, h


def getPointList(line):
    # Decode the line
    id, x, y, w, h = readLine(line)

    # Get the list of coordinates used by the rectangle
    pointList = set()
    for i in range(int(x), int(x) + int(w)):
        for j in range(int(y), int(y) + int(h)):
            pointList.add((i, j))

    return pointList


if __name__ == '__main__':
    # Load data
    data = load_data()

    # Get the list of points used by two or more rectangles
    pointSee = set()
    pointSeeTwice = set()
    for line in data:
        if len(pointSee) == 0:
            pointSee = getPointList(line)

        else:
            linePoints = getPointList(line)
            pointSeeTwice.update(pointSee.intersection(linePoints))
            pointSee.update(linePoints)

    print(len(pointSeeTwice))
