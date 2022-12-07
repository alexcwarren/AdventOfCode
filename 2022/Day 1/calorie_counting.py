from argparse import ArgumentParser
from os import path


class CalorieCounter:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "calorie_counting.py"
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
                f"Elf carrying the most calories is carrying {self.find_most_calories()}"
            )
        else:
            print(f"{self.find_top3_most_calories()}")

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

    def find_top3_most_calories(self) -> int:
        calories_sum: int = 0
        max_sums: list[int] = [0, 0, 0]

        with open(self.__filepath, "r") as file:
            for line in file:
                if line.strip().isdigit():
                    calories_sum += int(line)
                else:
                    if any(calories_sum > max_sum for max_sum in max_sums):
                        max_sums.remove(min(max_sums))
                        max_sums.append(calories_sum)
                    calories_sum = 0
        if any(calories_sum > max_sum for max_sum in max_sums):
            max_sums.remove(min(max_sums))
            max_sums.append(calories_sum)

        return sum(max_sums)


if __name__ == "__main__":
    CalorieCounter().print_result()
