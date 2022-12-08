# Day 3: Rucksack Reorganization

<https://adventofcode.com/2022/day/3>

## Table of Contents

1. [Part 1](#part-1)
   - [Problem Description](#problem-description-1)
   - [Solution Outline](#solution-outline-1)
1. [Part 2](#part-2)
   - [Problem Description](#problem-description-2)
   - [Solution Outline](#solution-outline-2)

## Part 1 {#part-1}

### Problem Description - Part 1 {#problem-description-1}

One Elf has the important job of loading all of the [rucksacks](https://en.wikipedia.org/wiki/Rucksack) with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large **compartments**. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, `a` and `A` refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

```python
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

- The first rucksack contains the items `vJrwpWtwJgWrhcsFMMfFFhFp`, which means its first compartment contains the items `vJrwpWtwJgWr`, while the second compartment contains the items `hcsFMMfFFhFp`. The only item type that appears in both compartments is lowercase **`p`**.
- The second rucksack's compartments contain `jqHRNqRjqzjGDLGL` and `rsFMfFZSrLrFZsSL`. The only item type that appears in both compartments is uppercase **`L`**.
- The third rucksack's compartments contain `PmmdzqPrV` and `vPwwTWBwg`; the only common item type is uppercase **`P`**.
- The fourth rucksack's compartments only share item type **`v`**.
- The fifth rucksack's compartments only share item type **`t`**.
- The sixth rucksack's compartments only share item type **`s`**.

To help prioritize item rearrangement, every item type can be converted to a **priority**:

- Lowercase item types `a` through `z` have priorities 1 through 26.
- Uppercase item types `A` through `Z` have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (`p`), 38 (`L`), 42 (`P`), 22 (`v`), 20 (`t`), and 19 (`s`); the sum of these is **`157`**.

Find the item type that appears in both compartments of each rucksack. **What is the sum of the priorities of those item types?**

### Solution Outline - Part 1 {#solution-outline-1}

#### Details

- Each line represents the **contents of a rucksack**.
- The **1st** and **2nd** *halves* of the rucksack's contents are in the **1st** and **2nd** *compartments*, respectively.
- There is exactly **one item** of the contents that is in **both** compartments
- **All** rucksack content items can **only** be comprised of *lowercase* and/or *UPPERCASE* letters
- Items are **case-sensitive**
- Each item has a priority:
  - **a - z** have priorities **1 - 26**
  - **A - Z** have priorities **27 - 52**

#### Goal(s)

- Find the one, **shared** item that is in both compartments for each rucksack
- Sum priority numbers for each shared item

#### Pseudocode

```python
from string import ascii_lowercase, ascii_uppercase
from collections import Counter

priority_numbers = {
    letter: number
    for number, letter in enumerate(ascii_lowercase + ascii_uppercase)
}

def solve_part1():
    shared_item_sum = 0
    foreach rucksack
        shared_item = find_shared_item(rucksack)
        shared_item_sum += priority_numbers[shared_item]
    return shared_item_sum

def find_shared_item(contents):
    num_items = len(contents)
    fst_half = contents[: num_items // 2]
    snd_half = contents[num_items // 2 :]
    for item in fst_half:
      if item in snd_half:
        return item
    return None
```

## Part 2 {#part-2}

### Problem Description - Part 2 {#problem-description-2}

As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the **only item type carried by all three Elves**. That is, if a group's badge is item type `B`, then all three Elves will have item type `B` somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is **common between all three Elves** in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

```python
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
```

And the second group's rucksacks are the next three lines:

```python
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

In the first group, the only item type that appears in all three rucksacks is lowercase `r`; this must be their badges. In the second group, their badge item type must be `Z`.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (`r`) for the first group and 52 (`Z`) for the second group. The sum of these is **`70`**.

Find the item type that corresponds to the badges of each three-Elf group. **What is the sum of the priorities of those item types?**

### Solution Outline - Part 2 {#solution-outline-2}

- Every 3 lines is a **group** of elves' rucksacks
- Find the item shared amongst **all 3** rucksacks
- Sum all group items' priority numbers

```python
def solve_part2():
    GROUP_SIZE = 3
    counter = 1
    group = list()
    foreach rucksack in input_file:
        if counter % 3 == 0:
            shared_item = find_shared_item(group)
            group.clear()
        else:
            group.append(rucksack)
        counter += 1

def find_shared_item(rucksacks):
    possible_shared_items = set()
    for i, rucksack in enumerate(rucksacks[1:]):
        items = possible_shared_items
        if i == 0:
            items = rucksack[0]
        elif i > 1 and len(possible_shared_items) == 1:
            return possible_shared_items[0]
        for item in items:
            if item in rucksack:
                possible_shared_items.append(item)
```
