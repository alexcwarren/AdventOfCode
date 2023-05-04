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

--- Part Two ---
Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""


def solve1(triangles: str) -> int:
    num_valid_triangles: int = 0
    for sides in triangles.splitlines():
        a, b, c = sorted(int(s) for s in sides.strip().split())
        if a + b > c:
            num_valid_triangles += 1
    return num_valid_triangles


def solve2(triangle_data: str) -> int:
    num_valid_triangles: int = 0
    lines: list[str] = triangle_data.splitlines()
    NUM_COLUMNS: int = len(lines[0].strip().split())
    triangle: list[int] = list()
    for col in range(NUM_COLUMNS):
        for line in lines:
            if len(triangle) < 3:
                triangle.append(int(line.strip().split()[col]))
            if len(triangle) == 3:
                a, b, c = sorted(triangle)
                if a + b > c:
                    num_valid_triangles += 1
                triangle.clear()
    return num_valid_triangles



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

    print("--- Part 2 ---")
    assert solve2(
        """  5  12 100
 10  10  99
 25  25 201
  3  30 200
  2  10 100
  4  25 101"""
    ) == 3
    with open(day3.input_path) as in_file:
        print(solve2(in_file.read()))
    print()
