from Day import Day

"""
--- Day 3: Squares With Three Sides ---
Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be a
graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but...
5 10 25? Some of these aren't triangles. You can't help but mark the impossible
ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""


def solve1(triangles: str) -> int:
    num_valid_triangles: int = 0
    for sides in triangles.splitlines():
        a, b, c = sorted(int(s) for s in sides.strip().split())
        if a + b > c:
            num_valid_triangles += 1
    return num_valid_triangles


def solve2():
    pass


if __name__ == "__main__":
    day3 = Day(__file__)

    print("--- Part 1 ---")
    assert solve1("5 10 25") == 0
    assert solve1(
        """3 2 4
12 10 25
30 10 25""") == 2
    with open(day3.input_path) as in_file:
        print(solve1(in_file.read()))
    print()
