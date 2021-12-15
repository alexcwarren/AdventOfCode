def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    lines = data.split('\n')

    template = lines[0]
    pairs = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in lines[2:]}
    return (template, pairs)


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


def part_one(template, pairs, using_sample=False):
    print(f'Running Part 1:')
    
    elem_set = set(pairs.values())
    elem_counts = {elem:template.count(elem) for elem in elem_set}
    
    total_steps = 10
    for __ in range(total_steps):
        new_template = ''
        for i,(elem1,elem2) in enumerate(zip(template[:-1], template[1:])):
            result = pairs[elem1 + elem2]
            new_template += f'{elem1}{result}'
            if i >= len(template) - 2:
                new_template += f'{elem2}'
            elem_counts[result] += 1
        template = new_template
    
    diff = max(count for count in elem_counts.values()) - min(count for count in elem_counts.values())

    if using_sample:
        verify_sample(diff, 1588)
    
    print(f'  Most common - Least common = {diff}\n')


def part_two(template, pairs, using_sample=False):
    print(f'Running Part 2:')
    
    elem_set = set(pairs.values())
    elem_counts = {elem:template.count(elem) for elem in elem_set}
    
    total_steps = 10
    # total_steps = 40
    for __ in range(total_steps):
        new_template = ''
        for i,(elem1,elem2) in enumerate(zip(template[:-1], template[1:])):
            result = pairs[elem1 + elem2]
            new_template += f'{elem1}{result}'
            if i >= len(template) - 2:
                new_template += f'{elem2}'
            elem_counts[result] += 1
        template = new_template
    
    diff = max(count for count in elem_counts.values()) - min(count for count in elem_counts.values())

    if using_sample:
        verify_sample(diff, 1588)
        # verify_sample(diff, 2188189693529)
    
    print(f'  Most common - Least common = {diff}\n')


if __name__ == '__main__':
    filename = 'sample.in'
    template, pairs = parse(filename)

    # part_one(template, pairs, filename == 'sample.in')

    part_two(template, pairs, filename == 'sample.in')