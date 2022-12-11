from argparse import ArgumentParser
from os import path


class CampCleanup:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "camp_cleanup.py"
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
            print(
                f"Number of ranges contained by another = {self.get_num_contained_ranges()}"
            )
        else:
            print(f"{self.solve_part2()}")

    def get_num_contained_ranges(self) -> int:
        num_contained_ranges: int = 0
        with open(self.__filepath, "r") as read_file:
            for pair in read_file:
                range1_str, range2_str = pair.strip().split(",")

                range1_id_a, range1_id_b = self.get_range_parameters(range1_str)
                range1 = range(range1_id_a, range1_id_b + 1)

                range2_id_a, range2_id_b = self.get_range_parameters(range2_str)
                range2 = range(range2_id_a, range2_id_b + 1)

                if all(id in range2 for id in range1) or all(
                    id in range1 for id in range2
                ):
                    num_contained_ranges += 1
        return num_contained_ranges

    def get_range_parameters(self, range_str) -> tuple:
        return (int(num) for num in range_str.split("-"))

    def solve_part2(self):
        pass


if __name__ == "__main__":
    CampCleanup().print_result()
