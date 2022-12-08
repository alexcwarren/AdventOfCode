from typing import Deque


def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return [int(d) for d in data.split(',') if d]


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


def part_one(fish, using_sample=False):
    print(f'Running Part 1:')
    
    NUM_DAYS = 80
    for __ in range(NUM_DAYS):
        new_fish = 0
        for f,fsh in enumerate(fish):
            if fsh == 0:
                fish[f] = 6
                new_fish += 1
                continue
            fish[f] -= 1
        fish.extend([8 for ___ in range(new_fish)])

    num_fish = len(fish)

    if using_sample:
        verify_sample(num_fish, 5934)
    
    print(f'  Number of fish after {NUM_DAYS} days = {num_fish}\n')


def part_two(fish, using_sample=False):
    print(f'Running Part 2:')
    
    NUM_DAYS = 256

    fish_timer_counts = Deque(fish.count(i) for i in range(9))
    for __ in range(NUM_DAYS):
        # Fish timer count (FTC) = i becomes FTC = i - 1
        fish_timer_counts.rotate(-1)

        # FTC = 0 create new fish, hence the 'rotate' above,
        # but the original FTC = 0 need to be put back at FTC = 6
        fish_timer_counts[6] += fish_timer_counts[8]

    num_fish = sum(fish_timer_counts)

    if using_sample:
        verify_sample(num_fish, 26984457539)
    
    print(f'  Number of fish after {NUM_DAYS} days = {num_fish}\n')


if __name__ == '__main__':
    filename = 'input.in'
    fish = parse(filename)

    part_one(fish, filename == 'sample.in')

    part_two(fish, filename == 'sample.in')