def parse(lines):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read()
    lines = data.split('\n')
    lines = [line.replace('->', '') for line in lines]

    coordinates = list()
    for line in lines:
        segment = list()
        for point in line.split():
            x,y = point.split(',')
            p = (int(x), int(y))
            segment.append(p)
        coordinates.append(tuple(segment))
    
    return coordinates


def part_one(coordinates):
    print(f'Running Part 1:')

    for coord in coordinates:
        print(coord)

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


def part_two(coordinates):
    print(f'Running Part 2:')

    

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'sample.in'
    coordinates = parse(filename)

    part_one(coordinates)

    # part_two(coordinates)