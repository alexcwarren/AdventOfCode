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


def part_two(binary_nums):
    print(f'Running Part 2:')
    
    O2_rating = calculate_rating(binary_nums, 1)
    CO2_rating = calculate_rating(binary_nums, 0)
        
    product = int(O2_rating, 2) * int(CO2_rating, 2)

    # # When using 'sample.in' data:
    # if O2_rating == '10111' and CO2_rating == '01010' and product == 230:
    #     print('SUCCESS')
    # else:
    #     print('FAILURE')
    
    print(f'    O2 rating = {O2_rating}, CO2 rating = {CO2_rating}')
    print(f'    ==> Product = {product}')


def calculate_rating(binary_nums, bit_criteria):
    binums = binary_nums.copy()
    bitA = str(bit_criteria)
    bitB = str(bit_criteria ^ 1)

    for i in range(len(binary_nums[0])):
        count0 = 0
        count1 = 0
        majority = len(binums) // 2 + 1

        for binum in binums:
            bit = binum[i]
            count0 += 1 if bit == '0' else 0
            count1 += 1 if bit == '1' else 0

            if count0 >= majority:
                binums = [b for b in binums if b[i] == bitB]
                break
            if count1 >= majority:
                binums = [b for b in binums if b[i] == bitA]
                break
        
        if count0 == count1:
            binums = [b for b in binums if b[i] == bitA]
        
        if len(binums) == 1:
            return binums[0]
    
    return '0'


if __name__ == '__main__':
    filename = 'input.in'
    parsed_lines = parse(filename)

    # part_one(parsed_lines)

    part_two(parsed_lines)