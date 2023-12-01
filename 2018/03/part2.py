from part1 import load_data, readLine


def getPointList(line):
    # Decode the line
    id, x, y, w, h = readLine(line)

    # Get the list of coordinates used by the rectangle
    pointList = []
    for i in range(int(x), int(x) + int(w)):
        for j in range(int(y), int(y) + int(h)):
            pointList.append([id, (i, j)])

    return pointList


if __name__ == '__main__':
    # Load data
    data = load_data()

    # Get the list of points used by two or more rectangles
    pointSee = []
    pointSeeTwice = []

    for line in data:
        print("DEBUG line id :", line.split(' ')[0])
        if len(pointSee) == 0:
            pointSee = getPointList(line)

        else:
            linePoints = getPointList(line)
            for point in linePoints:
                coord = point[1]
                for point2 in pointSee:
                    coord2 = point2[1]
                    if coord == coord2:
                        pointSeeTwice.append(point)
                        pointSeeTwice.append(point2)
            pointSee.extend(linePoints)

    # Remove duplicates
    pointSeeTwice = [list(t) for t in set(tuple(element) for element in pointSeeTwice)]

    # Get the points only seen once
    pointSeeOnce = [x for x in pointSee if x not in pointSeeTwice]

    # Get the ids
    ids = [x[0] for x in pointSeeOnce]
    ids = list(set(ids))

    print(ids)
