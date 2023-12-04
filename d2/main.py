import re

RED = 12
GREEN = 13
BLUE = 14

total = 0
power = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()

        m = re.match("Game (\d+):", line)
        assert m is not None
        gid = int(m.group(1))

        line = line.split(":")[1]
        records = line.split(";")

        maxblue = 0
        maxred = 0
        maxgreen = 0

        for record in records:
            def maxcolor(color, target):
                m = re.search(f"(\d+) {color}", record)
                if m is not None:
                    value = int(m.group(1))
                    if value > target:
                        return value
                return target

            maxblue = maxcolor("blue", maxblue)
            maxgreen = maxcolor("green", maxgreen)
            maxred = maxcolor("red", maxred)

        power += maxred * maxgreen * maxblue

        if maxblue <= BLUE and maxred <= RED and maxgreen <= GREEN:
            total += gid

print(f"total: {total}")
print(f"power: {power}")
