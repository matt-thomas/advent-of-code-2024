import re

all_lines = []
xmas_appearances = 0

with open("4.txt", "r") as file:
    for line in file:
      all_lines.append(line.strip())

# Iterate diagonally and vertically to look for XMAS
def check_for_xmas(horizontal_direction, vertical_direction, vertical_index, horizontal_index):
  for index2, char2 in enumerate(all_lines[vertical_index + vertical_direction]):
    if char2 == "M" and (horizontal_index - index2) == horizontal_direction:
      for index3, char3 in enumerate(all_lines[vertical_index + (vertical_direction * 2)]):
        if char3 == "A" and (index2 - index3) == horizontal_direction:
          for index4, char4 in enumerate(all_lines[vertical_index + (vertical_direction * 3)]):
            if char4 == "S" and (index3 - index4) == horizontal_direction:
              print(f"Found XMAS at horizontal indexes: {horizontal_index}, {index2}, {index3}, {index4} vertical index: {vertical_index}")
              return 1

  return 0

for i in range(len(all_lines)):
  line = all_lines[i]

  # First, find all instances of XMAS and SAMX.
  pattern = r"XMAS"

  # Use re.findall to find all in-line matches.
  matches = re.findall(pattern, line)
  count = len(matches)

  # Add to count.
  xmas_appearances += count

  # First, find all instances of XMAS and SAMX.
  pattern = r"SAMX"

  # Use re.findall to find all in-line matches.
  matches = re.findall(pattern, line)
  count = len(matches)

  # Add to count.
  xmas_appearances += count

  directions = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]  # Vertical and horizontal directions
  for index, char in enumerate(line):
    if char == 'X':
        for vertical_direction, horizontal_direction in directions:
            # Check boundary conditions
            if vertical_direction == 1 and (i + 4) <= len(all_lines):  # Downward
                xmas_appearances += check_for_xmas(horizontal_direction, vertical_direction, i, index)
            elif vertical_direction == -1 and i >= 3:  # Upward
                xmas_appearances += check_for_xmas(horizontal_direction, vertical_direction, i, index)

print(xmas_appearances)


