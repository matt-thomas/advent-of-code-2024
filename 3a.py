import re

with open("3.txt", "r") as file:
    running_total = 0
    for line in file:
        # print(line)

        # Regex pattern to match "mul(A,B)" where A and B are integers
        pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

        # Find all matches
        matches = re.findall(pattern, line)

        # Multiply A and B for each match
        products = [(int(a) * int(b)) for a, b in matches]

        running_total += sum(products)

print(running_total)
