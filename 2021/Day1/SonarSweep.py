def part_one():
    filename = 'input.in'
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    num_increases = 0
    lastval = None
    for line in lines:
        currval = int(line)

        if lastval is not None and currval > lastval:
            num_increases += 1
        
        lastval = currval
    
    print(f'Depth increased {num_increases} times\n')


def part_two():
    pass

if __name__ == '__main__':
    part_one()
    # part_two()