def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read()
    lines = data.split('\n')
    
    patterns = list()
    outputs = list()
    for line in lines:
        pattern, output = line.split(' | ')
        patterns.append(pattern.split())
        outputs.append(output.split())
    
    return (patterns, outputs)


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


def part_one(patterns_list, outputs, using_sample=False):
    print(f'Running Part 1:')
    
    # for i,seg in enumerate(digit_segments):
    #     print(f'#{i}: {seg}')
    # print()
    # for count,seg in unique_segments.items():
    #     print(f'#{digit_segments.index(seg)}: {seg} {count}')

    # print(patterns)
    # print(output)

    # segments = 'abcdefg'
    # signals = {seg: set(segments) for seg in segments}

    # patterns5 = [p for p in patterns if len(p) == 5]
    # index3 = 0
    # for i,p in enumerate(patterns5[1:], 1):
    #     if sum(1 for a,b in zip(p, patterns5[0]) if a != b) > 1:
    #         index3 = len(patterns5) - i # 2 if i=1, 1 if i=2
    #         break
    # for s in patterns5[index3]:
    #     signals[s] = signals[s].intersection(digit_segments[3])
    
    # for p in patterns:
    #     # If number of signals in p matches a unique digit
    #     len_p = len(p)
    #     if len_p in unique_segments:
    #         # print(f'Pattern={p}')
    #         # For each signal in p
    #         # for s in p:
    #         for s in segments:
    #             # print(f'{s}: {signals[s]} ==> ', end='')
    #             if s in p:
    #                 # Intersect signal's set of possible segments with segments of unique digit
    #                 signals[s] = signals[s].intersection(unique_segments[len_p])
    #             # print(f'{signals[s]}')
    #         # For each signal not in p
    #         # for s in set(segments).difference(p):
    #             # print(f'{s}: {signals[s]} ==> ', end='')
    #             else:
    #                 # Remove from signal's set of possible segments the segments of unique digit
    #                 # set.difference()
    #                 signals[s] = signals[s].difference(unique_segments[len_p])
    #         #     print(f'{signals[s]}')
    #         # print()
    
    # for s in (sig for sig in signals if 'f' in signals[sig]):
    #     if sum([p.count(s) for p in patterns]) == len(patterns) - 1:
    #         signals[s] = signals[s].intersection('f')
    #         break
    
    # for solved in [sig for sig in signals if len(signals[sig]) == 1]:
    #     for unsolved in [sig for sig in signals if len(signals[sig]) > 1]:
    #         signals[unsolved] = signals[unsolved].difference(signals[solved])
    
    # for s in signals:
    #     print(f'{s}: {signals[s]}')
    # # print([p.replace('d', 'A') for p in patterns])# if len(p) == 5])
    # # print([d.replace('a', 'A') for d in digit_segments])# if len(d) == 5])

    num_unique = 0
    for output in outputs:
        for digit in output:
            if len(digit) in unique_counts:
                num_unique += 1

    if using_sample:
        verify_sample(num_unique, 26)
    
    print(f'  Number of unique digits = {num_unique}\n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'input.in'
    patterns_list, outputs = parse(filename)

    # list of segments_used where index is the digit in question
    digit_segments = [
        'abcefg',  # 0
        'cf',      # 1
        'acdeg',   # 2
        'acdfg',   # 3
        'bcdf',    # 4
        'abdfg',   # 5
        'abdefg',  # 6
        'acf',     # 7
        'abcdefg', # 8
        'abcdfg',  # 9
    ]
    # count of segments needed for each digit
    counts = [len(seg) for seg in digit_segments]
    # digits with uniqe count of segments
    unique_counts = set([c for c in counts if counts.count(c) == 1])
    # dict of uniqe segment digits in segment_count:segments pairs
    unique_segments = {len(seg): seg for seg in digit_segments if len(seg) in unique_counts}

    part_one(patterns_list, outputs, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')