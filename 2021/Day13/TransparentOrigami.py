def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    lines = data.split('\n')

    dots = [{'x':int(line.split(',')[0]), 'y':int(line.split(',')[1])} for line in lines if ',' in line]
    folds = [(var, int(num)) for var,num in [line.replace('fold along ', '').split('=') for line in lines if 'fold' in line]]
    return (dots, folds)


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


def part_one(dots, folds, using_sample=False):
    print(f'Running Part 1:')

    for axis,value in folds:
        for dot in dots:
            if dot[axis] > value:
                dot[axis] = 2 * value - dot[axis]
        break # Only do one fold for this part
    
    num_dots = len(set((d['x'], d['y']) for d in dots))
    # output = [['.' for __ in range(20)] for ___ in range(20)]
    # for r,row in enumerate(output):
    #     for c,cell in enumerate(row):
    #         if {'x':c, 'y':r} in dots:
    #             print('#', end='')
    #         else:
    #             print(cell, end='')
    #     print()
    if using_sample:
        verify_sample(num_dots, 17)
    
    print(f'  Number of dots = {num_dots}\n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'input.in'
    dots, folds = parse(filename)

    part_one(dots, folds, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')