from argparse import ArgumentParser
from os import path


def find_most_calories(file_path: str):
    calories_sum: int = 0
    max_sum: int = 0

    with open(file_path, "r") as file:
        for line in file:
            if line.strip().isdigit():
                calories_sum += int(line)
            else:
                max_sum = max(calories_sum, max_sum)
                calories_sum = 0

    return max_sum


if __name__ == "__main__":
    prog_name: str = "calorie_counting.py"
    parser = ArgumentParser(
        prog=prog_name,
        description="",
        usage=f"python {prog_name} <filepath>",
    )
    parser.add_argument("filepath")
    args = parser.parse_args()

    if not path.isfile(args.filepath):
        print(f"ERROR: {args.filepath} does not exist")
    else:
        print(find_most_calories(args.filepath))
