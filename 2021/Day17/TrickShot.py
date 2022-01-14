from itertools import zip_longest


def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    axis_ranges = [d.strip() for d in data.split(':')[1].split(',')]
    return tuple(tuple(int(n) for n in ar.split('=')[1].split('..')) for ar in axis_ranges)


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


class Launchpad:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
    
    def launch_probes(self):
        pass

    def launch_probe(self, v_0x, v_0y):
        x = y = max_y = 0
        x_is_on_target = y_is_on_target = False
        for step in range(100):
            y += v_0y - step
            x = x + v_0x - step if x >= 0 else 0

            if self.is_x_on_target(x):
                x_is_on_target = True
            if self.is_y_on_target(y):
                y_is_on_target = True
            if ((x_is_on_target and not self.is_x_on_target(x))
                    or (y_is_on_target and not self.is_y_on_target(y))):
                break
            
            max_y = y if y > max_y else max_y
        
        return max_y
    
    def __is_on_target(self, axis, axis_range):
        return min(axis_range) <= axis <= max(axis_range)
    
    def is_x_on_target(self, x):
        return self.__is_on_target(x, self.x_range)
    
    def is_y_on_target(self, y):
        return self.__is_on_target(y, self.y_range)


def part_one(axis_ranges, using_sample=False):
    print(f'Running Part 1:')

    x_range, y_range = axis_ranges
    launchpad = Launchpad(x_range, y_range)
    '''
    Find ideal x:
    let x = avg(x_range) // 2
    let y = x
    
    '''

    # TODO
    # if using_sample:
    #     verify_sample()
    
    print(f'  \n')


def part_two(lines, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    axis_ranges = parse(filename)

    part_one(axis_ranges, filename == 'sample.in')

    # part_two(lines, filename == 'sample.in')