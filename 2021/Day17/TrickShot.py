def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    axis_ranges = [d.strip() for d in data.split(':')[1].split(',')]
    return tuple(tuple(int(n) for n in ar.split('=')[1].split('..')) for ar in axis_ranges)


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


def part_one(axis_ranges, using_sample=False):
    print(f'Running Part 1:')

    x_range, y_range = axis_ranges
    mid_x = sum(x_range) // 2
    
    for x1,x2 in zip(range(mid_x,0,-1), range(mid_x,max(x_range) + 1)):
        print(x1, x2)

    # TODO
    # if using_sample:
    #     verify_sample()
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    axis_ranges = parse(filename)

    part_one(axis_ranges, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')