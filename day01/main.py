from collections import Counter

with open("input.txt") as f:
    lines = [[int(i) for i in l.split()] for l in f]

# Part 1
l1, l2 = [sorted(x) for x in zip(*lines)]
print(sum(abs(a-b) for a, b in zip(l1, l2)))

# Part 2
counter = Counter(l2)
print(sum(i*counter[i] for i in l1))
