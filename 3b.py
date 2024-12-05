import re

with open("3.txt", "r") as file:
    running_total = 0

    content = file.read()

    # Regex pattern to match "mul(A,B)" where A and B are integers
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

    current_state = 1

    segments = re.split(r"(do\(\)|don't\(\))", content)

    for segment in segments:
        segment = segment.strip()

        if segment == "do()":
            current_state = 1
        elif segment == "don't()":
            current_state = 0

        if current_state == 1:
          # Find all matches
          matches = re.findall(pattern, segment)

          # Multiply A and B for each match
          products = [(int(a) * int(b)) for a, b in matches]

          running_total += sum(products)

print(running_total)
