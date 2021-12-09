def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return [int(d) for d in data.split(',')]


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
    
    print(lines)

    # TODO
    # if using_sample:
    #     verify_sample()
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    lines = parse(filename)

    part_one(lines, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')