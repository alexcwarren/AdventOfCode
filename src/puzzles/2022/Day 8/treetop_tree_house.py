from argparse import ArgumentParser
from os import path


class TreetopTreeHouse:
    def __init__(self, filepath: str = None, is_part1: bool = True):
        prog_name: str = "treetop_tree_house.py"
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

    def solve_part1(self):
        num_visible_trees: int = 0
        with open(self.__filepath, "r") as read_file:
            columns: list = None
            for line in (line.strip() for line in read_file):
                if columns is None:
                    columns = [""] * len(line)

                num_visible_trees += self.count_visible_trees(
                    [int(tree) for tree in line]
                )

                for i, char in enumerate(line):
                    columns[i] += char
            for col in columns:
                num_visible_trees += self.count_visible_trees(
                    [int(tree) for tree in col]
                )
        return num_visible_trees

    def count_visible_trees(self, tree_line: list) -> int:
        tallest_tree: int = max(tree_line)
        visible_trees_a: set = self.get_visible_tree_indices_forward(tree_line[:-1], tallest_tree)
        visible_trees_b: set = self.get_visible_tree_indices_backward(tree_line[1:], tallest_tree)
        return len(visible_trees_a.union(visible_trees_b))

    def get_visible_tree_indices_forward(self, tree_line: list, tallest_tree: int = 9) -> set:
        indices: set = set()
        curr_tallest_tree: int = tree_line[0]
        for i, tree in enumerate(tree_line[1:], 1):
            if tree > curr_tallest_tree:
                curr_tallest_tree = tree
                indices.add(i)
            if tree == tallest_tree:
                break
        return indices

    def get_visible_tree_indices_backward(self, tree_line: list, tallest_tree: int = 9) -> set:
        indices: set = set()
        last_index = len(tree_line) - 1
        curr_tallest_tree: int = tree_line[last_index]
        for i in range(last_index - 1, 0, -1):
            tree = tree_line[i]
            if tree > curr_tallest_tree:
                curr_tallest_tree = tree
                indices.add(i + 1)
            if tree == tallest_tree:
                break
        return indices

    def solve_part2(self):
        pass


if __name__ == "__main__":
    TreetopTreeHouse().print_result()
