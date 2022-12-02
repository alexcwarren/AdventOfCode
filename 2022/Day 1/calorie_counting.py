from argparse import ArgumentParser
from os import path


def find_most_calories(file_path: str):
    print(file_path)


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
        find_most_calories(args.filepath)
