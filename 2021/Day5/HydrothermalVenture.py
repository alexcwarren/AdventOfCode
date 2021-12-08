def parse(lines):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read()
    lines = data.split('\n')
    lines = [line.replace('->', '') for line in lines]

    coordinates = [(line.split()[0], line.split()[1]) for line in lines]
    print(coordinates)
    
    return []


def part_one():
    print(f'Running Part 1:')

    

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


def part_two():
    print(f'Running Part 2:')

    

    # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'sample.in'
    numbers_called, boards = parse(filename)

    # part_one(numbers_called, boards)

    part_two(numbers_called, boards)