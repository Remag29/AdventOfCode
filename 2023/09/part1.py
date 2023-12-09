def load_data():
    # load input.txt file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    # load data
    lines = load_data()

    fianl_result = 0

    for line in lines:

        values = [[int(x) for x in line.split(' ')]]
        print(values)

        while sum(values[-1]) != 0:
            result = []

            for i in range(len(values[-1])- 1):
                result.append(values[-1][i + 1] - values[-1][i])
            print(result)
            values.append(result)

        start = 0
        values.reverse()
        for value in values:
            start += value[-1]
        print(start)
        fianl_result += start

    print(fianl_result)
