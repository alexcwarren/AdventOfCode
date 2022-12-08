from argparse import ArgumentParser
from os import path


class RucksackReorganization:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "rucksack_reorganization.py"
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
            print(f"{self.sum_shared_item_priorities()}")
        else:
            print(f"{self.solve_part2()}")

    def sum_shared_item_priorities(self):
        pass

    def solve_part2(self):
        pass


if __name__ == "__main__":
    RucksackReorganization().print_result()
