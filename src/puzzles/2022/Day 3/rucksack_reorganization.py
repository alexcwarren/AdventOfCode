from argparse import ArgumentParser
from os import path
from string import ascii_letters


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
            print(
                f"Sum of priorities of shared items is {self.sum_shared_item_priorities()}"
            )
        else:
            print(f"{self.solve_part2()}")

    def sum_shared_item_priorities(self) -> int:
        prioritiy_numbers: dict[str, int] = {
            letter: number for number, letter in enumerate(ascii_letters, 1)
        }
        shared_item_sum: int = 0
        with open(self.__filepath, "r") as read_file:
            for rucksack_contents in read_file:
                shared_item: str = self.find_shared_item(rucksack_contents.strip())
                shared_item_sum += prioritiy_numbers[shared_item]
        return shared_item_sum

    def find_shared_item(self, contents: str) -> str:
        num_items: int = len(contents)
        fst_half: str = contents[:num_items // 2]
        snd_half: str = contents[num_items // 2:]
        for item in fst_half:
            if item in snd_half:
                return item
        return None

    def solve_part2(self):
        pass


if __name__ == "__main__":
    RucksackReorganization().print_result()
