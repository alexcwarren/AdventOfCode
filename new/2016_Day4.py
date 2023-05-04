from collections import Counter

from Day import Day

"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode the
list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a
(5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""


def solve1(room_data: str) -> int:
    sum_sector_ids: int = 0
    for line in room_data.splitlines():
        room, checksum = line[:-1].split("[")
        *room_name, sector_id = room.split("-")
        room_name_counter = Counter("".join(room_name))
        top_letters: list[str] = list(room_name_counter.keys())
        top_letters_str: str = "".join(
            sorted(
                sorted(top_letters), key=lambda x: room_name_counter[x], reverse=True
            )
        )
        if top_letters_str[:5] == checksum:
            sum_sector_ids += int(sector_id)
    return sum_sector_ids


def solve2():
    pass


if __name__ == "__main__":
    day4 = Day(__file__)

    print("--- Part 1 ---")
    assert (
        solve1(
            """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
        )
        == 1514
    )
    with open(day4.input_path) as in_file:
        print(solve1(in_file.read()))
    print()
