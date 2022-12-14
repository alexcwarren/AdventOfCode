from argparse import ArgumentParser
from os import path


class Directory:
    ROOT: str = "/"

    def __init__(self, name: str, parent_name: str = None):
        self.name: str = name
        self.parent_name: str = parent_name
        self.children: dict = dict()

    def add_child(self, child):
        self.children.setdefault(child.name, child)

    def get_size(self) -> int:
        size: int = 0
        for child in self.children:
            if isinstance(child, File) or child is File:
                size += child.size
            elif isinstance(child, Directory) or child is Directory:
                size += child.get_size()
            else:
                raise Exception(f"ERROR: Invalid type: {child}")
        return size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\"{self.name}\",\"{self.parent_name}\",{self.children})"

    def __str__(self) -> str:
        return f"{self.name} (dir)"


class File:
    def __init__(self, string: str):
        self.name: str = string.split()[1]
        self.size: int = int(string.split()[0])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\"{self.name}\",{self.size})"

    def __str__(self) -> str:
        return f"\"{self.size}\" {self.name}"


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
            args = string.split()
            self.type = args[1]
            if len(args) > 2:
                self.dir_name = args[2]

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
            curr_dir_name: str = None
            for line in (line.strip() for line in read_file):
                if self.Command.is_command(line):
                    command = self.Command(line)
                    if command.type == self.Command.TYPE.CD:
                        if command.dir_name == "..":
                            curr_dir_name = directories[curr_dir_name].parent_name
                        else:
                            directories[command.dir_name] = Directory(
                                command.dir_name, curr_dir_name
                            )
                            curr_dir_name = command.dir_name
                            # print(directories[curr_dir_name])
                    elif command.type == self.Command.TYPE.LS:
                        pass
                else:
                    child = None
                    if line.startswith("dir"):
                        dir_name: str = line.split()[1]
                        directories[dir_name] = Directory(
                            dir_name, directories[curr_dir_name]
                        )
                        child = directories[dir_name]
                    else:
                        child = File(line)
                    directories[curr_dir_name].add_child(child)

        for d in directories.values():
            print(d)
            print(repr(d))
            print()
        return 0
        # return sum(d.get_size() for d in directories.values() if d.get_size() <= max_size)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    NoSpaceLeftOnDevice().print_result()
