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
        self.parse_tree_heights_map()

        # All trees on the edge are visible
        num_visible_trees: int = 2 * self.num_rows + 2 * self.num_cols - 4

        for row, tree_line in enumerate(self.tree_heights_map[1:-1], 1):
            for col, tree_height in enumerate(tree_line[1:-1], 1):
                num_visible_trees += 1 if self.is_tree_visible(
                    tree_height, row, col
                ) else 0

        return num_visible_trees

    def parse_tree_heights_map(self):
        self.tree_heights_map: list = list()
        with open(self.__filepath, "r") as read_file:
            for line in read_file:
                tree_line: list = [int(tree_height) for tree_height in line.strip()]
                self.tree_heights_map.append(tree_line)
        self.num_rows: int = len(self.tree_heights_map)
        self.num_cols: int = len(self.tree_heights_map[0])

    def is_tree_visible(self, tree_height: int, row_idx: int, col_idx: int) -> bool:
        tree_line_row: list = self.tree_heights_map[row_idx]
        tree_line_col: list = [
            self.tree_heights_map[row][col_idx]
            for row in range(len(self.tree_heights_map))
        ]

        # Check other trees North of current tree
        tree_is_visible: bool = self.is_tree_visible_one_way(
            tree_height, tree_line_col[:row_idx]
        )
        if tree_is_visible: return True

        # Check other trees South of current tree
        tree_is_visible = tree_is_visible or self.is_tree_visible_one_way(
            tree_height, tree_line_col[row_idx + 1:]
        )
        if tree_is_visible: return True

        # Check other trees East of current tree
        tree_is_visible = tree_is_visible or self.is_tree_visible_one_way(
            tree_height, tree_line_row[col_idx + 1:]
        )
        if tree_is_visible: return True

        # Check other trees West of current tree
        tree_is_visible = tree_is_visible or self.is_tree_visible_one_way(
            tree_height, tree_line_row[:col_idx]
        )

        return tree_is_visible

    def is_tree_visible_one_way(self, tree_height: int, tree_line: list) -> bool:
        return all(other_tree_height < tree_height for other_tree_height in tree_line)

    def solve_part2(self):
        pass


if __name__ == "__main__":
    TreetopTreeHouse().print_result()
