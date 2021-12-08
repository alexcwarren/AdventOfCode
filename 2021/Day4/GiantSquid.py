def parse(lines):
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.read()
    return lines.split('\n')


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
    


    # # When using 'sample.in' data:
    # if ...:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    \n')


if __name__ == '__main__':
    filename = 'sample.in'
    parsed_lines = parse(filename)

    part_one(parsed_lines)

    # part_two(parsed_lines)