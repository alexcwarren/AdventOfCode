def parse(lines):
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.read()
    return lines.split('\n')


def part_one(commands):
    print(f'Running Part 1:')
    
    position_x = 0
    depth = 0

    for command in commands:
        direction, magnitude = command.split()
        magnitude = int(magnitude)
        
        if direction == 'forward':
            position_x += magnitude
        elif direction == 'down':
            depth += magnitude
        elif direction == 'up':
            depth -= magnitude
        else:
            print(f'ERROR: Invalid command direction: {direction}')
            return False
    
    product = position_x * depth
    
    print(f'    Horizontal position = {position_x}, Depth = {depth}')
    print(f'    ==> Product = {product}\n')


def part_two(commands):
    print(f'Running Part 2:')
    

    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'input.in'
    parsed_lines = parse(filename)

    part_one(parsed_lines)

    # part_two(parsed_lines)