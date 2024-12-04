import numpy as np

with open("input.txt") as f:
    arrs = [[int(i) for i in l.split()] for l in f]

def is_safe(d):
    return len(d[(d > 0) & (d <= 3)]) == len(d) or len(d[(d < 0) & (d >= -3)]) == len(d)

part1 = 0
part2 = 0
for a in arrs:
    if is_safe(np.diff(a)):
        part1 += 1
        part2 += 1
    else:
        for i in range(len(a)):
            if is_safe(np.diff(a[:i]+a[i+1:])):
                part2 += 1
                break
print(part1)
print(part2)
