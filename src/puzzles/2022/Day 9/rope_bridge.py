from argparse import ArgumentParser
from os import path


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.__coords = [self.x, self.y]

    def delta_x(self, other) -> int:
        return self.x - other.x

    def delta_y(self, other) -> int:
        return self.y - other.y

    def is_not_adjacent_to(self, other) -> bool:
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __iter__(self) -> tuple:
        for coord in self.__coords:
            yield coord

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class RopeBridge:
    MOVES = {
        "U": Coordinate(0, -1),
        "D": Coordinate(0, 1),
        "L": Coordinate(-1, 0),
        "R": Coordinate(1, 0),
    }

    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "rope_bridge.py"
        self.is_part1: bool = is_part1

        # Look for command-line args if no filepath provided
        if filepath is None:
            parser = ArgumentParser(
                prog=prog_name,
                usage=f"python {prog_name} -f <filepath> -p <partnumber>",
            )
            parser.add_argument("-f", "--filepath")
            parser.add_argument("-p", "--partnumber", choices=["1", "2"], default="1")
            args = parser.parse_args()
            filepath = args.filepath
            self.is_part1 = args.partnumber == "1"

        if filepath is None:
            print("ERROR: filepath not provided.")
            exit()
        elif not path.isfile(filepath):
            print('ERROR: "{filepath}" does not exist.')
            exit()
        else:
            self.__filepath: str = filepath

    def print_result(self):
        if self.is_part1:
            print(f"{self.solve_part1()}")
        else:
            print(f"{self.solve_part2()}")

    def solve_part1(self, delta_threshold: int = 1):
        head: Coordinate = Coordinate(0, 0)
        tail: Coordinate = Coordinate(0, 0)

        tail_visits: set = set()
        with open(self.__filepath, "r") as read_file:
            for line in read_file:
                move_dir, num_repeats = self.parse_motion(line)
                curr_move: Coordinate = self.MOVES[move_dir]
                for _ in range(num_repeats):
                    head += curr_move
                    delta_x = head.delta_x(tail)
                    delta_y = head.delta_y(tail)
                    if max(abs(delta_x), abs(delta_y)) > delta_threshold:
                        if head.is_not_adjacent_to(tail):
                            if abs(delta_x) > abs(delta_y):
                                tail += Coordinate(0, delta_y)
                            else:
                                tail += Coordinate(delta_x, 0)
                        tail += curr_move
                    tail_visits.add(tuple(tail))
        return len(tail_visits)

    def parse_motion(self, line: str) -> tuple:
        motion: list = line.strip().split(" ")
        return motion[0], int(motion[1])

    def solve_part2(self):
        pass


if __name__ == "__main__":
    RopeBridge().print_result()
