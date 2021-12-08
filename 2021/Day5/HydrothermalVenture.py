def parse(lines):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read()
    lines = data.split('\n')
    lines = [line.replace('->', '') for line in lines]

    segments = list()
    for line in lines:
        segment = list()
        for point in line.split():
            x,y = point.split(',')
            p = (int(x), int(y))
            segment.append(p)
        segments.append(tuple(segment))
    
    return segments


def part_one(segments):
    print(f'Running Part 1:')

    maxval = max([max([max(c) for c in coords]) for coords in segments])
    print(maxval)

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


def part_two(segments):
    print(f'Running Part 2:')

    

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'sample.in'
    segments = parse(filename)

    part_one(segments)

    # part_two(segments)