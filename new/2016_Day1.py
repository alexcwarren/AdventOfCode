from collections import deque
from Day import Day


"""
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the
clock's oscillator is regulated by stars. Unfortunately, the stars have been
stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve
all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day
in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!
You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter Bunny
Recruiting Document the Elves intercepted start here, and nobody had time to
work them out further.
The Document indicates that you should start at the given coordinates (where you
just landed) and face North. Then, follow the provided sequence: either turn
left (L) or right (R) 90 degrees, then walk forward the given number of blocks,
ending at a new intersection.
There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?

For example:

- Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks
away.
- R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2
blocks away.
- R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

--- Part Two ---
Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

class Common:
    SIDE_MAP: dict[str, int] = {
        "R": -1,
        "L": 1
    }
    HORIZONTAL: str = "EW"
    NEGATIVE: str = "WS"

    def __init__(self):
        self.directions: deque = deque("NESW")
        print(self.directions)

    def direction(self):
        return self.directions[0]


def solve1(instructions: str) -> int:
    c = Common()
    num_blocks: int = 0
    x: int = 0
    y: int = 0
    for instruction in instructions.replace(" ", "").split(","):
        side, *distance_str = instruction
        distance: int = int("".join(distance_str))
        c.directions.rotate(c.SIDE_MAP[side])
        if c.direction() in c.HORIZONTAL:
            x += distance * (-1 if c.direction() == "W" else 1)
        else:
            y += distance * (-1 if c.direction() == "S" else 1)
    num_blocks = abs(x) + abs(y)
    return num_blocks


def solve2(instructions: str) -> int:
    c = Common()
    pos: list[int] = [0, 0]
    visited: dict[tuple[int], bool] = {(0, 0): True}
    for instruction in instructions.replace(" ", "").split(","):
        side, *distance_str = instruction
        distance: int = int("".join(distance_str))
        c.directions.rotate(c.SIDE_MAP[side])
        sign: int = 1
        if c.direction() in c.NEGATIVE:
            sign = -1
        for _ in range(1, distance + 1):
            if c.direction() in c.HORIZONTAL:
                pos[0] += sign
            else:
                pos[1] += sign
            pos_tuple = tuple(pos)
            if pos_tuple in visited:
                return sum(abs(p) for p in pos)
            visited[pos_tuple] = True
    return 0


if __name__ == "__main__":
    day1 = Day(__file__)

    print("--- Part 1 ---")
    assert solve1("R2, L3") == 5
    assert solve1("R2, R2, R2") == 2
    assert solve1("R5, L5, R5, R3") == 12
    with open(day1.input_path) as in_file:
        print(f"{solve1(in_file.read())} blocks")
    print()

    print("--- Part 2 ---")
    assert solve2("R8, R4, R4, R8") == 4
    with open(day1.input_path) as in_file:
        print(f"{solve2(in_file.read())} blocks")
    print()
