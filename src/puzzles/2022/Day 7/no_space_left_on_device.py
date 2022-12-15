from argparse import ArgumentParser
from os import path


class Node:
    def __init__(self, name: str, parent_dir):
        self.name: str = name
        self.parent_dir: Node = parent_dir


class Directory(Node):
    def __init__(self, name: str, parent_dir: Node):
        super().__init__(name, parent_dir)
        self.children: dict = dict()

    def add_child(self, child: Node):
        self.children.setdefault(child.name, child)

    def get_size(self) -> int:
        size: int = 0
        for child in self.children.values():
            if isinstance(child, Directory):
                size += child.get_size()
            elif isinstance(child, File):
                size += child.size
        return size

    def is_root_dir(self) -> bool:
        return self.parent_dir is None

    def __repr__(self) -> str:
        return f"{self.name} (dir, size={self.get_size()})"


class File(Node):
    def __init__(self, name: str, size: int, parent_dir: Node):
        super().__init__(name, parent_dir)
        self.size: int = size

    def __repr__(self) -> str:
        return f"{self.name} (file, size={self.size})"


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

    def sum_sizes_of_directories(self, max_size: int = 100_000):
        directories: dict = dict()
        root_dir: Node = None
        with open(self.__filepath, "r") as read_file:
            curr_dir: Node = None
            for i, line in enumerate(line.strip() for line in read_file):
                try:
                    if self.Command.is_command(line):
                        command = self.Command(line)
                        if command.type == self.Command.TYPE.CD:
                            if command.dir_name == "/":
                                root_dir = Directory(command.dir_name, None)
                                directories[root_dir.name] = root_dir
                                curr_dir = directories[root_dir.name]
                            elif command.dir_name == "..":
                                curr_dir = curr_dir.parent_dir
                            else:
                                directories.setdefault(command.dir_name, Directory(command.dir_name, curr_dir))
                                curr_dir = directories[command.dir_name]
                        elif command.type == self.Command.TYPE.LS:
                            continue
                    else:
                        child_node: Node = None
                        name: str = line.split()[1]
                        if line.startswith("dir"):
                            directories.setdefault(name, Directory(name, curr_dir))
                            child_node = directories[name]
                        else:
                            file_size: int = int(line.split()[0])
                            child_node = File(name, file_size, curr_dir)
                        curr_dir.add_child(child_node)
                except Exception as exc:
                    print(i, f"\"{line}\"")
                    print(exc)
                    return 0

        return sum(d.get_size() for d in directories.values() if d.get_size() <= max_size)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    NoSpaceLeftOnDevice().print_result()
