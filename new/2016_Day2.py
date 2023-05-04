from Day import Day

"""
--- Day 2: Bathroom Security ---
You arrive at Easter Bunny Headquarters under cover of darkness. However, you
left in such a rush that you forgot to use the bathroom! Fancy office buildings
like this one usually have keypad locks on their bathrooms, so you search the
front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will
no longer be written down. Instead, please memorize and follow the procedure
below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad: U
moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or, for
the first line, the "5" button); press whatever button you're on at the end of
each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk
to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9

Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and
stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then
down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with
5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front
desk. What is the bathroom code?

--- Part Two ---
You finally arrive at the bathroom (it's a several minute walk from the lobby so
visitors can behold the many fancy conference rooms and water coolers on this
floor) and go to punch in the code. Much to your bladder's dismay, the keypad is
not at all like you imagined it. Instead, you are confronted with the result of
hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge, but given the same
instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at
5.
Continuing from "5", you move right twice and down three times (through "6",
"7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"),
ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom
code?
"""


class Common:
    VAL: str = "val"
    U: str = "U"
    D: str = "D"
    L: str = "L"
    R: str = "R"


def solve1(instructions: str) -> str:
    code: str = ""
    c = Common()
    KEY1: dict[str, int] = {c.VAL: 1, c.U: 1, c.D: 4, c.L: 1, c.R: 2}
    KEY2: dict[str, int] = {c.VAL: 2, c.U: 2, c.D: 5, c.L: 1, c.R: 3}
    KEY3: dict[str, int] = {c.VAL: 3, c.U: 3, c.D: 6, c.L: 2, c.R: 3}
    KEY4: dict[str, int] = {c.VAL: 4, c.U: 1, c.D: 7, c.L: 4, c.R: 5}
    KEY5: dict[str, int] = {c.VAL: 5, c.U: 2, c.D: 8, c.L: 4, c.R: 6}
    KEY6: dict[str, int] = {c.VAL: 6, c.U: 3, c.D: 9, c.L: 5, c.R: 6}
    KEY7: dict[str, int] = {c.VAL: 7, c.U: 4, c.D: 7, c.L: 7, c.R: 8}
    KEY8: dict[str, int] = {c.VAL: 8, c.U: 5, c.D: 8, c.L: 7, c.R: 9}
    KEY9: dict[str, int] = {c.VAL: 9, c.U: 6, c.D: 9, c.L: 8, c.R: 9}
    KEYS: dict[int, dict] = {
        1: KEY1,
        2: KEY2,
        3: KEY3,
        4: KEY4,
        5: KEY5,
        6: KEY6,
        7: KEY7,
        8: KEY8,
        9: KEY9,
    }
    key_val: int = 5
    for line in instructions.split("\n"):
        for move in line:
            key_val = KEYS[key_val][move]
        code += str(key_val)
    return code


def solve2(instructions: str) -> str:
    return ""


if __name__ == "__main__":
    day2 = Day(__file__)

    print("--- Part 1 ---")
    assert (
        solve1(
            """ULL
RRDDD
LURDL
UUUUD"""
        )
        == "1985"
    )
    with open(day2.input_path) as in_file:
        print(f"{solve1(in_file.read())}")
    print()

    print("--- Part 2 ---")
    assert solve2(
        """ULL
RRDDD
LURDL
UUUUD"""
    ) == "5DB3"
