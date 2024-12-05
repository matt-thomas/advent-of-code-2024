import re

all_lines = []
xmas_appearances = 0

with open("4.txt", "r") as file:
    for line in file:
      all_lines.append(line.strip())

for vertical_index in range(len(all_lines)):
  line = all_lines[vertical_index]

  for index, char in enumerate(line):
    # Only check starting on line 1 and ending on the penultimate line.
    if 1 <= vertical_index < len(all_lines) and char == 'A':
       # TODO Check above for "M S" and "S M"
       # TODO Check below for "M S" and "S M"

print(xmas_appearances)


