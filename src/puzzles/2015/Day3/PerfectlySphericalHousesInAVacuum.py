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
    
    for i,(a,e) in enumerate(zip(actual_vals, expected_vals), 1):
        if a != e:
            print(f'#{i} FAILED: Expected {e} got {a}')
            return False
    
    print('SUCCESS')
    return True


coord = lambda x,y : (x, y)
direction = {
    '^': coord(0, -1),
    'v': coord(0, 1),
    '>': coord(1, 0),
    '<': coord(-1, 0)
}


def part_one(lines, using_sample=False):
    print(f'Running Part 1:')
    
    x,y = 0,0
    coordinates_list = list()

    for i,line in enumerate(lines):
        coordinates_list.append({(x,y): 1})
        for ch in line:
            x2,y2 = direction[ch]
            x += x2
            y += y2
            coordinates_list[i][(x,y)] = coordinates_list[i].get((x,y), 0) + 1
    
    unique_visits = [len(d) for d in coordinates_list]

    if using_sample:
        verify_sample(unique_visits, [2, 4, 2])
    
    print(f'  {unique_visits}\n')


def part_two(lines, using_sample=False):
    print(f'Running Part 2:')

    coordinates_list = list()
    for line in lines:
        x,y = {1: 0, 2: 0}, {1: 0, 2: 0}
        coordinates1 = {(x[1],y[1]): 1}
        coordinates2 = dict()
        coordinates = {1: coordinates1, 2: coordinates2}

        for i,ch in enumerate(line):
            x2,y2 = direction[ch]
            s = i % 2 + 1
            x[s] += x2
            y[s] += y2
            coordinates[s][(x[s],y[s])] = coordinates[s].get((x[s],y[s]), 0) + 1
        
        coordinates_list.append(coordinates)
    
    unique_visits = [
        len(set([k for k in coords[1]] + [k for k in coords[2]]))
        for coords in coordinates_list
    ]

    if using_sample:
        verify_sample(unique_visits, [3, 3, 11])
    
    print(f'  {unique_visits}\n')


if __name__ == '__main__':
    filename = 'input.in'
    lines = parse(filename)

    # part_one(lines, filename == 'sample.in')

    part_two(lines, filename == 'sample.in')