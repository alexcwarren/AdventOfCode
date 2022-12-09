from argparse import ArgumentParser
from functools import singledispatchmethod
from os import path
from string import ascii_letters


class RucksackReorganization:
    prioritiy_numbers: dict[str, int] = {
        letter: number for number, letter in enumerate(ascii_letters, 1)
    }

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
            print(
                f"Sum of priorities of group type item is {self.sum_group_type_item_priorities()}"
            )

    def sum_shared_item_priorities(self) -> int:
        shared_item_sum: int = 0
        with open(self.__filepath, "r") as read_file:
            for rucksack_contents in read_file:
                shared_item: str = self.find_shared_item(rucksack_contents.strip())
                shared_item_sum += self.prioritiy_numbers[shared_item]
        return shared_item_sum

    @singledispatchmethod
    def find_shared_item(self, collection):
        raise NotImplementedError

    @find_shared_item.register
    def find_shared_item_given_str(self, contents: str) -> str:
        num_items: int = len(contents)
        fst_half: str = contents[: num_items // 2]
        snd_half: str = contents[num_items // 2:]
        for item in fst_half:
            if item in snd_half:
                return item
        return None

    def sum_group_type_item_priorities(self, group_size: int = 3) -> int:
        group_type_item_sum: int = 0
        with open(self.__filepath, "r") as read_file:
            group: list[str] = list()
            for i, rucksack_contents in enumerate(
                (line.strip() for line in read_file), 1
            ):
                if not i % 3:
                    group.append(rucksack_contents)
                    shared_item: str = self.find_shared_item(group)
                    group_type_item_sum += self.prioritiy_numbers[shared_item]
                    group.clear()
                else:
                    group.append(rucksack_contents)
        return group_type_item_sum

    @find_shared_item.register
    def find_shared_item_given_list(self, rucksacks: list) -> str:
        rucksacks: list[set] = [set(rucksack) for rucksack in rucksacks]
        possible_shared_items = set()
        for i, rucksack_items in enumerate(rucksacks[1:]):
            if i > 0 and len(possible_shared_items) == 1:
                return possible_shared_items.pop()

            items = possible_shared_items.copy() if i > 0 else rucksacks[0]
            possible_shared_items.clear()
            for item in items:
                if item in rucksack_items:
                    possible_shared_items.add(item)
        return possible_shared_items.pop() if len(possible_shared_items) > 0 else None


if __name__ == "__main__":
    RucksackReorganization().print_result()
