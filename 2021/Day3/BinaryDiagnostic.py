def parse(lines):
    lines = None
    with open(filename, 'r') as infile:
        lines = infile.read()
    return lines.split('\n')


def part_one(binary_nums):
    print(f'Running Part 1:')
    
    gamma_rate = ''
    epsilon_rate = ''

    MAJORITY = len(binary_nums) // 2 + 1
    WIDTH = len(binary_nums[0])

    for i in range(WIDTH):
        count0 = 0
        count1 = 0

        for binum in binary_nums:
            bit = binum[i]
            count0 += 1 if bit == '0' else 0
            count1 += 1 if bit == '1' else 0

            if count0 >= MAJORITY:
                gamma_rate += '0'
                epsilon_rate += '1'
                break
            if count1 >= MAJORITY:
                gamma_rate += '1'
                epsilon_rate += '0'
                break
    
    product = int(gamma_rate, 2) * int(epsilon_rate, 2)

    # When using 'sample.in' data:
    # if gamma_rate == '10110' and epsilon_rate == '01001' and product == 198:
    #     print('SUCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    Gamma rate = {gamma_rate}, Epsilon rate = {epsilon_rate}')
    print(f'    ==> Product = {product}')


def part_two():
    print(f'Running Part 2:')

    

    print(f'    \n')


if __name__ == '__main__':
    filename = 'input.in'
    parsed_lines = parse(filename)

    part_one(parsed_lines)

    # part_two(parsed_lines)