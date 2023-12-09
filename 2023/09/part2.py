from part1 import load_data

if __name__ == '__main__':
    # load data
    lines = load_data()

    fianl_result = 0

    for line in lines:

        values = [[int(x) for x in line.split(' ')]]

        while sum(values[-1]) != 0:
            result = []

            for i in range(len(values[-1]) - 1):
                result.append(values[-1][i + 1] - values[-1][i])
            values.append(result)

        start = 0
        values.reverse()
        for value in values:
            # Test if all values are the same
            if len(set(value)) == 1:
                start = value[0]
            else:
                start = value[0] - start
        fianl_result += start

    print(fianl_result)
