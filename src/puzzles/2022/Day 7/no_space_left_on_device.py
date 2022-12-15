from argparse import ArgumentParser
from collections import defaultdict
from itertools import accumulate
from os import path


class NoSpaceLeftOnDevice:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "no_space_left_on_device.py"
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
            print(f"{self.sum_sizes_of_directories()}")
        else:
            print(f"{self.solve_part2()}")

    def sum_sizes_of_directories(self, max_size: int = 100_000):
        directory_sizes = defaultdict(int)
        with open(self.__filepath, "r") as read_file:
            dir_list: list = list()
            for line in (line.strip() for line in read_file):
                match line.split():
                    case "$", "cd", "/":
                        dir_list.append("/")
                    case "$", "cd", "..":
                        dir_list.pop()
                    case "$", "cd", d:
                        dir_list.append(f"{d}/")
                    case "dir", dir_path:
                        pass
                    case "$", "ls":
                        pass
                    case size, dir_path:
                        for dir_path in accumulate(dir_list):
                            directory_sizes[dir_path] += int(size)

        return sum(size for size in directory_sizes.values() if size <= max_size)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    NoSpaceLeftOnDevice().print_result()
