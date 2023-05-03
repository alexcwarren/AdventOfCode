from argparse import ArgumentParser
from os import path


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def to_tuple(self) -> tuple:
        return tuple(self.x, self.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class RopeBridge:
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
        tail_visits: set = set()

        with open(self.__filepath, "r") as read_file:
            head = Coordinate(0, 0)
            tail = Coordinate(0, 0)

            for line in read_file:
                move, num_repeats = self.parse_motion(line)
                for _ in range(num_repeats):
                    if abs(head.x - tail.x) > delta_threshold or abs(head.y - tail.y) > delta_threshold:
                        if head.x != tail.x and head.y != tail.y:
                            pass
                            # Move diagonally
                        else:
                            # Move vertically/horizontally
                            tail += move
                        tail_visits.add(tail)


    def parse_motion(self, line: str) -> tuple:
        parameters = line.strip().split(" ")
        return parameters[0], int(parameters[1])

    def solve_part2(self):
        pass


if __name__ == "__main__":
    RopeBridge().print_result()
