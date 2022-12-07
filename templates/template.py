from argparse import ArgumentParser
from os import path
from sys import argv


class REPLACE_WITH_CLASS_NAME:
    def __init__(self, filepath: str = None):
        prog_name: str = "REPLACE_WITH_PROBLEM_NAME.py"

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
        print(f"{self.solve_problem()}")

    def solve_problem(self):
        pass


if __name__ == "__main__":
    dayREPLACE_WITH_DAY_NUMBER = REPLACE_WITH_CLASS_NAME().print_result()
