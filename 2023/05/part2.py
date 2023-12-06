from part1 import load_data, get_tables

if __name__ == '__main__':
    # Load data
    lines = load_data()

    # Get tables
    tables = get_tables(lines)
    print(tables)

    # Get seeds
    seeds = tables[0][0].split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    print(seeds)

    mappings = []
    for line in lines[2:]:
        line = line.strip()
        if line.endswith(":"):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(" ")])
    print(mappings)

    # Get the final position
    res = 2 ** 64
    for s, o in zip(seeds[::2], seeds[1::2]):
        ranges = [(s, s + o - 1)]
        for typemappings in mappings:
            newranges = []
            for l, h in ranges:
                found = False
                for md, ms, mo in typemappings:
                    if l >= ms and h < ms + mo:
                        newranges.append((l - ms + md, h - ms + md))
                        found = True
                    elif l < ms <= h < ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + h - ms))
                        found = True
                    elif h >= ms + mo > l >= ms:
                        ranges.append((ms + mo, h))
                        newranges.append((md + l - ms, md + mo - 1))
                        found = True
                    elif l < ms and h >= ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + mo - 1))
                        ranges.append((ms + mo, h))
                        found = True
                    if found == True:
                        break
                if not found:
                    newranges.append((l, h))
            ranges = newranges.copy()
        res = min(res, min(ranges)[0])

    # Get the lowest seed position
    print('-------------------')
    print('Lowest seed position : ' + str(res))
