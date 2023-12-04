import re
from collections import defaultdict

total = 0

lines = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()

        m = re.match("Card\s+(\d+):", line)
        if m is None:
            print(line)
        assert m is not None
        cid = int(m.group(1))

        line = line.split(":")[1]
        lines.append(line)

    for n, line in enumerate(lines):
        wins = line.split("|")[0].split()
        cards = line.split("|")[1].split()

        matches = list(set(wins) & set(cards))

        points = 0
        if len(matches) > 0:
            points = 1 << (len(matches) - 1)

        total += points

    counts = defaultdict(int)
    for n, line in enumerate(lines):
        wins = line.split("|")[0].split()
        cards = line.split("|")[1].split()

        counts[n] += 1

        matches = list(set(wins) & set(cards))

        for i in range(len(matches)):
            counts[n + i + 1] += counts[n]

    print(counts)

print(f"total: {total}")
print(f"count: {sum(counts.values())}")
