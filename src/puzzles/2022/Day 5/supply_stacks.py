from argparse import ArgumentParser
from os import path
from re import search, findall
from collections import deque


class SupplyStacks:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "supply_stacks.py"
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

    def solve_part1(self) -> str:
        self.EMPTY_CRATE: str = "[ ]"

        rows: list = list()
        num_stacks: int = 0
        with open(self.__filepath, "r") as read_file:
            rows, num_stacks = self.parse_crate_rows(read_file)
            # for line in (line.rstrip() for line in read_file):
            #     if line is None:
            #         break
            #     if search(r"\d+", line):
            #         num_stacks = max(int(num) for num in findall(r"\d+", line))
            #         break

            #     crates: list = list()
            #     crate: str = ""
            #     skip_next_space: bool = False
            #     for i,char in enumerate(line):
            #         if skip_next_space:
            #             skip_next_space = False
            #             continue

            #         crate += char

            #         if i == len(line) - 1 or len(crate) == CRATE_SIZE:
            #             crate = self.EMPTY_CRATE if " " in crate else crate
            #             crates.append(crate)
            #             crate = ""
            #             skip_next_space = True

            #     crates.extend(self.EMPTY_CRATE for _ in range(CRATE_SIZE - len(crates)))
            #     rows.append(crates)
        # print("\n".join(",".join(row) for row in rows))

        stacks = self.transpose_rows_to_stacks(rows, num_stacks)
        print("\n".join(",".join(stack) for stack in stacks))

        return ""

    def parse_crate_rows(self, crate_data_file, crate_size: int = 3) -> tuple:
        rows: list = list()
        num_stacks: int = 0
        for line in (line.rstrip() for line in crate_data_file):
            if line is None:
                break
            if search(r"\d+", line):
                num_stacks = max(int(num) for num in findall(r"\d+", line))
                break

            crates: list = list()
            crate: str = ""
            skip_next_space: bool = False
            for i,char in enumerate(line):
                if skip_next_space:
                    skip_next_space = False
                    continue

                crate += char

                if i == len(line) - 1 or len(crate) == crate_size:
                    crate = self.EMPTY_CRATE if " " in crate else crate
                    crates.append(crate)
                    crate = ""
                    skip_next_space = True

            crates.extend(self.EMPTY_CRATE for _ in range(crate_size - len(crates)))
            rows.append(crates)
        return rows, num_stacks

    def transpose_rows_to_stacks(self, rows: list, num_stacks: int) -> list:
        stacks: list = [deque() for _ in range(num_stacks)]
        for row in rows:
            for c, col in enumerate(row):
                if col != self.EMPTY_CRATE:
                    stacks[c].appendleft(col)
        return stacks

    def solve_part2(self):
        pass


if __name__ == "__main__":
    SupplyStacks().print_result()
