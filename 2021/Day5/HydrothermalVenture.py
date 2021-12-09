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

    MAXVAL = max([max([max(c) for c in coords]) for coords in segments])
    grid = [[0 for __ in range(MAXVAL + 1)] for __ in range(MAXVAL + 1)]
    
    for seg in segments:
        (x1,y1), (x2,y2) = seg

        # Horizontal lines
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                grid[y][x1] += 1

        # Vertical lines
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                grid[y1][x] += 1
    
    num_overlaps = 0
    for row in grid:
        num_overlaps += len([num for num in row if num > 1])

    # for row in grid:
    #     for num in row:
    #         if num == 0:
    #             print('.', end='')
    #         else:
    #             print(num, end='')
    #     print()
    # print()

    # When using 'sample.in' data:
    # if num_overlaps == 5:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    Number of overlaps = {num_overlaps}\n')


def part_two(segments):
    print(f'Running Part 2:')

    

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'input.in'
    segments = parse(filename)

    part_one(segments)

    # part_two(segments)