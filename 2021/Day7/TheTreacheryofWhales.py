def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return [int(d) for d in data.split(',')]


def verify_sample(actual_vals, expected_vals):
    if isinstance(actual_vals, list):
        if len(actual_vals) != len(expected_vals):
            print('ERROR: Count of actual values != count of expected values:', end=' ')
            print(f'len(actual_vals)={len(actual_vals)}, len(expected_vals)={len(expected_vals)}')
            return False
    else:
        actual_vals = [actual_vals]
        expected_vals = [expected_vals]
    
    for a,e in zip(actual_vals, expected_vals):
        if a != e:
            print(f'FAILED: Expected {e} got {a}')
            return False
    
    print('SUCCESS')
    return True


def part_one(positions, using_sample=False):
    print(f'Running Part 1:')

    least_fuel_spent = None
    for p in range(0, max(positions) + 1):
        fuel_spent = sum([abs(p - posn) for posn in positions])

        if least_fuel_spent is None or fuel_spent < least_fuel_spent:
            least_fuel_spent = fuel_spent
        elif fuel_spent > least_fuel_spent:
            break

    if using_sample:
        verify_sample(least_fuel_spent, 37)
    
    print(f'  Least fuel spent = {least_fuel_spent}\n')


def part_two(positions, using_sample=False):
    print(f'Running Part 2:')

    least_fuel_spent = None
    for p in range(0, max(positions) + 1):
        fuel_spent = sum([abs(p - posn) * (abs(p - posn) + 1) // 2 for posn in positions])

        if least_fuel_spent is None or fuel_spent < least_fuel_spent:
            least_fuel_spent = fuel_spent
        elif fuel_spent > least_fuel_spent:
            break

    if using_sample:
        verify_sample(least_fuel_spent, 168)
    
    print(f'  Least fuel spent = {least_fuel_spent}\n')


if __name__ == '__main__':
    filename = 'input.in'
    positions = parse(filename)

    part_one(positions, filename == 'sample.in')

    part_two(positions, filename == 'sample.in')