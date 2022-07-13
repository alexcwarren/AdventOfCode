def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data.split('\n')


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


def part_one(lines, using_sample=False):
    print(f'Running Part 1:')
    
    for line in lines:
        dimensions = line.split('x')
        print(dimensions)
        length, width, height = dimensions
        print(length, width, height)

    # TODO
    # if using_sample:
    #     verify_sample(paper_areas, [58, 43])
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    lines = parse(filename)

    part_one(lines, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')