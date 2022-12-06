from argparse import ArgumentParser
from os import path
from sys import argv


class CalorieCounter:
    def __init__(self, filepath: str = None):
        prog_name: str = "calorie_counting.py"

        # Look for command-line args if no filepath provided
        if filepath is None:
            parser = ArgumentParser(
                prog=prog_name,
                usage=f"python {prog_name} -f <filepath>",
            )
            parser.add_argument("-f", "--filepath")
            args = parser.parse_args()
            filepath: str = args.filepath

        if filepath is None:
            print("ERROR: filepath not provided.")
            exit()
        elif not path.isfile(filepath):
            print(f'ERROR: "{filepath}" does not exist.')
            exit()
        else:
            self.__filepath: str = filepath

    def print_result(self):
        print(f"Elf carrying the most calories is carrying {self.find_most_calories()}")

    def find_most_calories(self) -> int:
        calories_sum: int = 0
        max_sum: int = 0

        with open(self.__filepath, "r") as file:
            for line in file:
                if line.strip().isdigit():
                    calories_sum += int(line)
                else:
                    max_sum = max(calories_sum, max_sum)
                    calories_sum = 0

        return max_sum


if __name__ == "__main__":
    day1 = CalorieCounter().print_result()
