def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    patterns, output = data.split(' | ')

    patterns = tuple(patterns.split())
    output = tuple(output.split())

    return (patterns, output)


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


def part_one(patterns, output, using_sample=False):
    print(f'Running Part 1:')
    
    # for i,seg in enumerate(digit_segments):
    #     print(f'#{i}: {seg}')
    # print()
    # for count,seg in unique_segments.items():
    #     print(f'#{digit_segments.index(seg)}: {seg} {count}')

    print(patterns)
    # print(output)

    segments = 'abcdefgh'
    signals = {seg: set(segments) for seg in segments}
    
    for p in patterns:
        if len(p) in unique_counts:
            for s in p:
                signals[s] = signals[s].intersection(unique_segments[len(p)])
            for s in [sig for sig in signals if sig not in p]:
                signals[s].remove()
    print(signals)

    # TODO
    # if using_sample:
    #     verify_sample()
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample_small.in'
    patterns, output = parse(filename)

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

    part_one(patterns, output, filename == 'sample_small.in')

    # part_two(lines, filename == 'sample.in')