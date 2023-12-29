from collections import defaultdict
from copy import deepcopy
import sys
from typing import Dict, List, Tuple

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "Days of Advent Code\Day 22\input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append([tuple(int(a) for a in l.split(",")) for l in line.split("~")])

    return lines


def intersects(l1, r1, l2, r2):
    return not (r1[0] < l2[0] or l1[0] > r2[0] or r1[1] < l2[1] or l1[1] > r2[1])

def can_remove_2(brick, above, below, falling):
    if brick in falling:
        return
    else:
        falling.add(brick)
        for brick_above in above[brick]:
            if len(below[brick_above] - falling) == 0:
                can_remove_2(brick_above, above, below, falling)


def solve():
    lines = read_lines_to_list()
    lines.sort(key=lambda line: line[0][2])

    levels = defaultdict(list)
    bricks = []
    for _itx, (a, b) in enumerate(lines):
        (ca, cb) = (a, b)
        while ca[2] > 0:
            new_position = ((ca[0], ca[1], ca[2] - 1), (cb[0], cb[1], cb[2] - 1))
            invalid_level = False

            for cl, cr in levels[new_position[0][2]]:
                if intersects(
                    new_position[0],
                    new_position[1],
                    cl,
                    cr,
                ):
                    invalid_level = True
                    break

            if invalid_level:
                break
            else:
                (ca, cb) = new_position

        for level in range(ca[2], cb[2] + 1):
            levels[level].append(((ca[0], ca[1], ca[2]), (cb[0], cb[1], cb[2])))
        bricks.append((ca, cb))

    bricks_above = defaultdict(set)
    bricks_below = defaultdict(set)
    for brick in bricks:
        if brick[0][2] + 1 in levels:
            for candidates in levels[brick[0][2] - 1]:
                if intersects(brick[0], brick[1], candidates[0], candidates[1]):
                    bricks_above[candidates].add(brick)
                    bricks_below[brick].add(candidates)

    part_two = 0

    for brick in bricks:
        will_fall = set()
        can_remove_2(brick, bricks_above, bricks_below, will_fall)
        part_two += len(will_fall) - 1

    print(f"Part 2: {part_two}")


solve()