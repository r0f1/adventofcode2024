from operator import add, mul
from itertools import product

with open("input.txt") as f:
    lines = [x.strip().split(": ") for x in f]

for is_part1 in [True, False]:
    if is_part1:
        allowed_ops = [add, mul]
    else:
        allowed_ops = [add, mul, lambda a, b: int(f"{a}{b}")]

    res = 0
    for chunk1, chunk2 in lines:
        expected_result = int(chunk1)
        args = [int(c) for c in chunk2.split()]

        for ops in product(allowed_ops, repeat=len(args)-1):
            curr_res = args[0]
            for arg, op in zip(args[1:], ops):
                curr_res = op(curr_res, arg)
            if curr_res == expected_result:
                res += curr_res
                break
    print(res)
