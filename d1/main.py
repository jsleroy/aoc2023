import re

def f(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
    x = re.findall(r'(\d)', line)
    return int(x[0] + x[-1])

print(sum(map(f, open('input.txt'))))

# total = 0
# 
# mapping = {
#     "one":   "1e",
#     "two":   "2o",
#     "three": "3e",
#     "four":  "4r",
#     "five":  "5e",
#     "six":   "6x",
#     "seven": "7n",
#     "eight": "8t",
#     "nine":  "9e",
# }
# 
# with open("input.txt", "r") as f:
#     for line in f:
#         line = line.strip()
#         oline = line
# 
#         for k, v in mapping.items():
#             line = line.replace(k, v)
# 
#         for c in line:
#             if c.isdigit():
#                 value = int(c) * 10
#                 break
# 
#         for c in reversed(line):
#             if c.isdigit():
#                 value += int(c)
#                 break
# 
#         print(oline, line, value)
# 
#         total += value
# 
# print(total)
