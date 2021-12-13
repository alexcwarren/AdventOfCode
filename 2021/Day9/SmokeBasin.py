def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return [[int(d) for d in datum] for datum in data.split('\n')]


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


def part_one(heightmap, using_sample=False):
    print(f'Running Part 1:')

    risk_level = 0
    
    LAST_R = len(heightmap) - 1
    for r,row in enumerate(heightmap):
        LAST_C = len(row) - 1
        for c,height in enumerate(row):
            #                     RIGHT   DOWN   LEFT     UP
            for (mod_r,mod_c) in ((0,1), (1,0), (0,-1), (-1,0)):
                adj_r = r + mod_r
                adj_c = c + mod_c
                if (0 <= adj_r <= LAST_R and 0 <= adj_c <= LAST_C
                           and height >= heightmap[adj_r][adj_c]):
                    break
            else:
                risk_level += height + 1

    if using_sample:
        verify_sample(risk_level, 15)
    
    print(f'  Risk level = {risk_level}\n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'input.in'
    heightmap = parse(filename)

    part_one(heightmap, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')