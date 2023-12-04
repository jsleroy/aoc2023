import collections
import math
import re

W = 140

parts = collections.defaultdict(list)
board = list(open('input.txt'))
chars = {(r, c) for r in range(W) for c in range(W) if board[r][c] not in "01234566789."}

for r, row in enumerate(board):
    for n in re.finditer("\d+", row):
        edge = {(r, c) for r in (r - 1, r, r + 1) for c in range(n.start() - 1, n.end() + 1)}

        for o in edge & chars:
            parts[o].append(int(n.group(0)))

print(sum(sum(p) for p in parts.values()))
print(sum(math.prod(p) for p in parts.values() if len(p) == 2))
