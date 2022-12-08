def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return data.split('\n')


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


def part_one(lines, using_sample=False):
    print(f'Running Part 1:')
    
    char_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    total_score = 0

    type_stack = list()
    for line in lines:
        for chr in line:
            if chr in chars:
                type_stack.append(chars[chr])
            elif chr != type_stack.pop():
                total_score += char_scores[chr]
                break

    if using_sample:
        verify_sample(total_score, 26397)
    
    print(f'  Total score = {total_score}\n')


def part_two(lines, using_sample=False):
    print(f'Running Part 2:')

    char_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    line_scores = list()

    for line in lines.copy():
        type_stack = list()
        is_corrupted = False
        for chr in line:
            if chr in chars:
                type_stack.append(chars[chr])
            elif chr != type_stack.pop():
                lines.remove(line)
                is_corrupted = True
                break
        if is_corrupted:
            continue

        total_score = 0
        for chr in reversed(type_stack):
            total_score *= 5
            total_score += char_scores[chr]
        line_scores.append(total_score)
    
    line_scores.sort()
    mid = len(line_scores) // 2
    middle_score = line_scores[mid]


    if using_sample:
        verify_sample(middle_score, 288957)
    
    print(f'  Middle score = {middle_score}\n')


if __name__ == '__main__':
    filename = 'input.in'
    lines = parse(filename)

    chars = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    part_one(lines, filename == 'sample.in')

    part_two(lines, filename == 'sample.in')