def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return tuple(tuple(line.split('-')) for line in data.split('\n'))


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


def part_one(connections, using_sample=[False,False,False]):
    print(f'Running Part 1:')
    
    path = ''
    node = START
    for cxn1,cxn2 in (c for c in connections if node in c):
        path += node
        node = cxn1 if cxn1 != node else cxn2

    # TODO
    # if using_sample[0]:
    #     verify_sample(num_paths, 10)
    # if using_sample[1]:
    #     verify_sample(num_paths, 19)
    # if using_sample[2]:
    #     verify_sample(num_paths, 226)
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample_small.in'
    connections = parse(filename)
    START = 'start'

    part_one(connections, [filename == file for file in ('sample_small.in', 'sample.in', 'sample_large.in')])

    # part_two(lines, filename == 'sample.in')