def parse(lines):
    pass


def part_one(lines):
    print(f'Running Part 1:')
    
    position_x = 0
    depth = 0
    
    print(f'    Horizontal position = {position_x}, Depth = {depth}')
    print(f'    ==> Product = {position_x * depth}\n')


def part_two(lines):
    print(f'Running Part 2:')
    

    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'sample.in'
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    
    parsed_lines = parse(lines)

    part_one(parsed_lines)

    # part_two(parsed_lines)