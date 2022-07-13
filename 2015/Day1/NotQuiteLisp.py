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
    
    instruction = {
        "(": 1,
        ")": -1
    }
    final_floors = list()

    for line in lines:
        floor = 0
        for ch in line:
            floor += instruction[ch]
        final_floors.append(floor)

    if using_sample:
        verify_sample(final_floors, [0, 0, 3, 3, 3, -1, -1, -3, -3])
    
    print(f'  {final_floors}\n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'input.in'
    lines = parse(filename)

    part_one(lines, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')