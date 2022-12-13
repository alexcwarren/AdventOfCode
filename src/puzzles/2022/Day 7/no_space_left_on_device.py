from argparse import ArgumentParser
from os import path


class Directory:
    def __init__(self, name: str):
        self.name: str = name
        self.children: dict = dict()

    def add_child(self, child):
        self.children.setdefault(child.name, child)

    def get_size(self) -> int:
        size: int = 0
        for child in self.children:
            if isinstance(child, File):
                size += child.size
            elif isinstance(child, Directory):
                size += child.get_size()
            else:
                raise Exception(f"ERROR: Invalid type: {child}")
        return size


class File:
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size


class NoSpaceLeftOnDevice:
    class Command:
        class TYPE:
            CD: str = "cd"
            LS: str = "ls"

        def __init__(self, string: str):
            self.type: str = None

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

    def sum_sizes_of_directories(self, max_size: int = 10000):
        directories: dict = dict()
        with open(self.__filepath, "r") as read_file:
            curr_dir: Directory = None
            for line in read_file:
                command = self.Command(line)
                if command.type == self.Command.TYPE.CD:
                    # TODO Attempt to create new Directory
                    pass
                elif command.type == self.Command.TYPE.LS:
                    # TODO Add children to curr_dir
                    pass
        return sum(d.get_size() for d in directories if d.get_size() <= max_size)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    NoSpaceLeftOnDevice().print_result()
