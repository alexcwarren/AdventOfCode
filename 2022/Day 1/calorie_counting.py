from argparse import ArgumentParser
from os import path


class CalorieCounter:
    def __init__(self, filepath: str = None):
        prog_name: str = "calorie_counting.py"
        parser = ArgumentParser(
            prog=prog_name,
            usage=f"python {prog_name} <filepath>",
        )
        parser.add_argument("filepath")
        args = parser.parse_args()

        if not path.isfile(args.filepath):
            print(f"ERROR: {args.filepath} does not exist")
        else:
            self.__filepath: str = args.filepath

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
    result: int = CalorieCounter().find_most_calories()
    print(result)
