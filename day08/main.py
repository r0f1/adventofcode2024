from collections import defaultdict
from itertools import combinations, count

with open("input.txt") as f:
    lines = [x.strip() for x in f]

bounds = len(lines)

d = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            d[c].append((x, y))

all_locations = set.union(*[set(x) for x in d.values()])

for is_part1 in [True, False]:
    antinodes = set()
    for locations in d.values():
        for (xa, ya), (xb, yb) in combinations(locations, 2):
            dx, dy = xa - xb, ya - yb

            for i in count(1):
                nx, ny = xa + i*dx, ya + i*dy
                mx, my = xb - i*dx, yb - i*dy

                added = False
                if 0 <= nx < bounds and 0 <= ny < bounds:
                    antinodes.add((nx, ny))
                    added = True
                if 0 <= mx < bounds and 0 <= my < bounds:
                    antinodes.add((mx, my))
                    added = True

                if is_part1 or not added:
                    break

    if is_part1:
        print(len(antinodes))
    else:
        print(len(antinodes | all_locations))
