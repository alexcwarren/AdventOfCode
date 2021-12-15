from typing import List


def parse(filename):
    data = None
    with open(filename, 'r') as infile:
        data = infile.read().strip()
    return [[int(d) for d in datum] for datum in data.split('\n')]


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


def print_octopuses(octos):
    for row in octos:
        for octo in row:
            print(octo, end='')
        print()
    print()


class Octopus:
        FLASH_THRESHOLD = 9
        MAX_ROW = 0
        MAX_COL = 0

        def __init__(self, level, coordinates):
            self.level = level
            self.flashed = False
            self.row, self.col = coordinates
            self.__adjacents_coords = self.__determine_adjacents()
            self.adjacents = list()
        
        def __determine_adjacents(self):
            adjacents = list()
            # f g h
            # e x a
            # d c b               a      b      c       d       e       f        g       h
            for mod_r,mod_c in ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)):
                adj_r = self.row + mod_r
                adj_c = self.col + mod_c
                if 0 <= adj_r <= Octopus.MAX_ROW and 0 <= adj_c <= Octopus.MAX_COL:
                    adjacents.append((adj_r,adj_c))
            return tuple((r,c) for r,c in adjacents)
        
        def assign_adjacents(self, octos_list):
            for r,c in self.__adjacents_coords:
                self.adjacents.append(octos_list[r][c])
        
        def step(self):
            if self.flashed:
                return 0
            
            self.level += 1

            if self.level > Octopus.FLASH_THRESHOLD:
                return self.flash()
            return 0
        
        def flash(self):
            if self.flashed:
                return 0
            self.flashed = True
            self.level = 0

            num_adj_flashes = 0
            for adj_oct in self.adjacents:
                num_adj_flashes += adj_oct.step()
            return 1 + num_adj_flashes

        def reset(self):
            self.flashed = False
        
        def __str__(self):
            return f'{self.level}'
        
        def __repr__(self):
            string =  f'Octopus[{self.row}][{self.col}]:\n'
            string += f'  level={self.level} flashed={self.flashed}\n'
            string += f'  adjacents={self.adjacents}\n'
            return string


class OctopusList(List):
    def __init__(self, levels):
        super().__init__([[Octopus(level, (r,c)) for c,level in enumerate(row)] for r,row in enumerate(levels)])
        for row in self:
            for octo in row:
                octo.assign_adjacents(self)


def part_one(octopus_levels, using_sample=False):
    print(f'Running Part 1:')
    
    Octopus.MAX_ROW = len(octopus_levels) - 1
    Octopus.MAX_COL = len(octopus_levels[Octopus.MAX_ROW]) - 1
    octopuses = OctopusList(octopus_levels)

    num_steps = 100
    num_flashes = 0
    for __ in range(1, num_steps + 1):
        for row in octopuses:
            for octo in row:
                num_flashes += octo.step()
        for row in octopuses:
            for octo in row:
                octo.reset()

    if using_sample:
        verify_sample(num_flashes, 1656)
    
    print(f'  Number of flashes = {num_flashes}\n')


def part_two(octopus_levels, using_sample=False):
    pass


if __name__ == '__main__':
    filename = 'sample.in'
    octopus_levels = parse(filename)

    part_one(octopus_levels, filename == 'sample.in')

    # part_two(octopus_levels, filename == 'sample.in')