def part_one(lines):
    print(f'Running Part 1:')
    num_increases = 0
    lastval = None
    for line in lines:
        currval = int(line)

        if lastval is not None and currval > lastval:
            num_increases += 1
        
        lastval = currval
    
    print(f'    Depth increased {num_increases} times\n')


def part_two(lines):
    print(f'Running Part 2:')
    N = len(lines)
    last_sum = None
    num_increases = 0

    for i,(lineA,lineB,lineC) in enumerate(zip(lines[:N - 2], lines[1:N - 1], lines[2:])):
        a,b,c = int(lineA),int(lineB),int(lineC)
        curr_sum = a + b + c
        # print(f'{a} + {b} + {c} = {curr_sum}')
        if last_sum is not None and curr_sum > last_sum:
            # print(f'{curr_sum} > {last_sum}')
            num_increases += 1
        last_sum = curr_sum
    
    print(f'    Depth increased {num_increases} times\n')


if __name__ == '__main__':
    filename = 'input.in'
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    
    # part_one(lines)

    part_two(lines)