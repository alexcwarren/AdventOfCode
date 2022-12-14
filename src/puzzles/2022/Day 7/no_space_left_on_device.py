from argparse import ArgumentParser
from os import path


class Directory:
    def __init__(self, name: str, parent = None):
        self.name: str = name
        self.parent = None
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
    def __init__(self, string: str):
        self.name: str = None
        self.size: int = None


class NoSpaceLeftOnDevice:
    class Command:
        class TYPE:
            CD: str = "cd"
            LS: str = "ls"

        def __init__(self, string: str):
            self.__parse_string(string)

        @staticmethod
        def is_command(string: str) -> bool:
            return string.startswith("$")

        def __parse_string(self, string: str):
            # TODO Remove "$"
            args = string.split()
            self.type = args[0]
            if len(args) > 1:
                self.dir_name = args[1]

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
            curr_dir: str = None
            for line in read_file:
                if self.Command.is_command(line):
                    command = self.Command(line)
                    if command.type == self.Command.TYPE.CD:
                        if command.dir_name == "..":
                            curr_dir = curr_dir.parent.dir_name
                        else:
                            directories[command.dir_name] = Directory(command.dir_name)
                            curr_dir = command.dir_name
                    elif command.type == self.Command.TYPE.LS:
                        pass
                else:
                    child = None
                    if line.startswith("dir"):
                        directories["TODO"] = Directory(line)
                        child = directories["TODO"]
                    else:
                        child = File(line)
                    directories[curr_dir].add_child(child)

        return sum(d.get_size() for d in directories if d.get_size() <= max_size)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    NoSpaceLeftOnDevice().print_result()
