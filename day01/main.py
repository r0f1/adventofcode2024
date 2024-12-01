from collections import Counter
from heapq import heapify, heappop

with open("input.txt") as f:
    lines = [[int(i) for i in l.split()] for l in f]

# Part 1
l1, l2 = [list(x) for x in zip(*lines)]
heapify(l1)
heapify(l2)

res = 0
while l1:
    res += abs(heappop(l1)-heappop(l2))
print(res)

# Part 2
l1, l2 = zip(*lines)
counter = Counter(l2)
print(sum(i*counter[i] for i in l1))
