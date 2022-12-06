from argparse import ArgumentParser
from os import path
from sys import argv


class RockPaperScissors:
    def __init__(self, filepath: str = None):
        prog_name: str = "rock_paper_scissors.py"

        # If at least one command-line argument was passed
        if len(argv) > 1:
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
    day2 = RockPaperScissors().print_result()
