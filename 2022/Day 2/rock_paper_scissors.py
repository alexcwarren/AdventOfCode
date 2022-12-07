from argparse import ArgumentParser
from os import path


class RockPaperScissors:
    class CHOICES:
        ROCK: int = 1
        PAPER: int = 2
        SCISSORS: int = 3

    A: str = "A"
    B: str = "B"
    C: str = "C"
    X: str = "X"
    Y: str = "Y"
    Z: str = "Z"

    choices_map: dict[str, int] = dict()
    choices_map[A] = choices_map[X] = CHOICES.ROCK
    choices_map[B] = choices_map[Y] = CHOICES.PAPER
    choices_map[C] = choices_map[Z] = CHOICES.SCISSORS

    class OUTCOMES:
        LOSE: int = 0
        DRAW: int = 3
        WIN: int = 6

    outcomes_map: dict[str, int] = dict()
    outcomes_map[X] = OUTCOMES.LOSE
    outcomes_map[Y] = OUTCOMES.DRAW
    outcomes_map[Z] = OUTCOMES.WIN

    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "rock_paper_scissors.py"
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
            print(f"Your total score is {self.determine_total_score_1()}")
        else:
            print(f"{self.get_total_score_2()}")

    def determine_total_score_1(self):
        total_score: int = 0
        with open(self.__filepath, "r") as readfile:
            for line in readfile:
                opponent, you = (item.upper() for item in line.strip().split())
                opponent_choice = self.choices_map[opponent]
                your_choice = self.choices_map[you]
                round_score = your_choice + self.get_outcome(
                    your_choice, opponent_choice
                )
                total_score += round_score
        return total_score

    def get_outcome(self, you: int, opponent: int) -> int:
        if you == opponent:
            return self.OUTCOMES.DRAW
        if you == self.CHOICES.ROCK and opponent == self.CHOICES.SCISSORS:
            return self.OUTCOMES.WIN
        if you == self.CHOICES.SCISSORS and opponent == self.CHOICES.ROCK:
            return self.OUTCOMES.LOSE
        if you > opponent:
            return self.OUTCOMES.WIN
        return self.OUTCOMES.LOSE

    def determine_total_score_2(self):
        pass

    def derive_choice(self, opponent: int, outcome: int) -> int:
        pass


if __name__ == "__main__":
    RockPaperScissors().print_result()
