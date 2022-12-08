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


def print_grid(grid):
    for row in grid:
        for num in row:
            if num == 0:
                print('.', end='')
            else:
                print(num, end='')
        print()
    print()


def verify_sample(actual_vals, expected_vals):
    if isinstance(actual_vals, list):
        if len(actual_vals) != len(expected_vals):
            print('ERROR: Count of actual values != count of expected values:', end=' ')
            print(f'len(actual_vals)={len(actual_vals)}, len(expected_vals)={len(expected_vals)}')
            return False
    else:
        actual_vals = [actual_vals]
        expected_vals = [expected_vals]
    
    for a,e in zip(actual_vals, expected_vals):
        if a != e:
            print(f'FAILED: Expected {e} got {a}')
            return False
    
    print('SUCCESS')
    return True


def part_one(segments, using_sample=False):
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

    # print_grid(grid)

    if using_sample:
        verify_sample(num_overlaps, 5)
    
    print(f'  Number of overlaps = {num_overlaps}\n')


def part_two(segments, using_sample=False):
    print(f'Running Part 2:')

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
        
        # Diagonal lines
        elif abs(x2 - x1) == abs(y2 - y1):
            xstep = 1 if x2 > x1 else -1
            xstart = min(x1,x2) if xstep > 0 else max(x1,x2)
            xstop = (max(x1,x2) if xstep > 0 else min(x1,x2)) + xstep

            ystep = 1 if y2 > y1 else -1
            ystart = min(y1,y2) if ystep > 0 else max(y1,y2)
            ystop = (max(y1,y2) if ystep > 0 else min(y1,y2)) + ystep
            
            for x,y in zip(range(xstart, xstop, xstep), range(ystart, ystop, ystep)):
                grid[y][x] += 1

    # print_grid(grid)
    
    num_overlaps = 0
    for row in grid:
        num_overlaps += len([num for num in row if num > 1])

    if using_sample:
        verify_sample(num_overlaps, 12)
    
    print(f'  Number of overlaps = {num_overlaps}\n')


if __name__ == '__main__':
    filename = 'input.in'
    segments = parse(filename)

    part_one(segments, filename == 'sample.in')

    part_two(segments, filename == 'sample.in')