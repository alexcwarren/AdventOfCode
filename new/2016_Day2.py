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
"""


class Common:
    __VAL: str = "val"
    __U: str = "U"
    __D: str = "D"
    __L: str = "L"
    __R: str = "R"
    KEY1: dict[str, int] = {__VAL: 1, __U: 1, __D: 4, __L: 1, __R: 2}
    KEY2: dict[str, int] = {__VAL: 2, __U: 2, __D: 5, __L: 1, __R: 3}
    KEY3: dict[str, int] = {__VAL: 3, __U: 3, __D: 6, __L: 2, __R: 3}
    KEY4: dict[str, int] = {__VAL: 4, __U: 1, __D: 7, __L: 4, __R: 5}
    KEY5: dict[str, int] = {__VAL: 5, __U: 2, __D: 8, __L: 4, __R: 6}
    KEY6: dict[str, int] = {__VAL: 6, __U: 3, __D: 9, __L: 5, __R: 6}
    KEY7: dict[str, int] = {__VAL: 7, __U: 4, __D: 7, __L: 7, __R: 8}
    KEY8: dict[str, int] = {__VAL: 8, __U: 5, __D: 8, __L: 7, __R: 9}
    KEY9: dict[str, int] = {__VAL: 9, __U: 6, __D: 9, __L: 8, __R: 9}
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


def solve1(instructions: str) -> str:
    code: str = ""
    c = Common()
    key_val: int = 5
    for line in instructions.split("\n"):
        for move in line:
            key_val = c.KEYS[key_val][move]
        code += str(key_val)
    return code


def solve2():
    pass


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
