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


def part_two(heightmap, using_sample=False):
    print(f'Running Part 2:')

    N,W,E,S = 'N','W','E','S'
    boundary = {N:False, W:False, E:False, S:False}
    MAX_HEIGHT = 9

    basin_sizes = list()
    basin_size = 0
    LAST_R = len(heightmap) - 1
    for r,row in enumerate(heightmap):
        LAST_C = len(row) - 1
        boundary[N] = r == 0
        boundary[S] = r == LAST_R
        for c,height in enumerate(row):
            boundary[W] = c == 0
            boundary[E] = c == LAST_C
            #                                            EAST  SOUTH   WEST    NORTH
            for dir,(mod_r,mod_c) in zip((E, S, W, N), ((0,1), (1,0), (0,-1), (-1,0))):
                adj_r = r + mod_r
                adj_c = c + mod_c
                
                if (0 <= adj_r <= LAST_R and 0 <= adj_c <= LAST_C
                           and heightmap[adj_r][adj_c] == MAX_HEIGHT):
                    boundary[dir] = True
            if all((boundary[b] for b in boundary)):
                # TODO
                # Append basin_size
                basin_sizes.append(basin_size)
                # Reset basin_size
                basin_size = 0
                # Reset boundaries
                

    if using_sample:
        verify_sample()
    
    print(f'  \n')


if __name__ == '__main__':
    filename = 'input.in'
    heightmap = parse(filename)

    # part_one(heightmap, filename == 'sample.in')

    part_two(heightmap, filename == 'sample.in')