import re

all_lines = []
xmas_appearances = 0

with open("4.txt", "r") as file:
    for line in file:
      all_lines.append(line.strip())

for vertical_index in range(len(all_lines)):
  line = all_lines[vertical_index]

  # Only check starting on line 1 and ending on the penultimate line.
  if 1 <= vertical_index < (len(all_lines) - 1):
    for index, char in enumerate(line):
      if 1 <= index < len(line) - 1 and char == 'A':
        # print(f"Checking line {vertical_index}, char {index}")

        # Extract above and below snippets
        diag1 = all_lines[vertical_index - 1][index - 1] + char + all_lines[vertical_index + 1][index + 1]
        diag2 = all_lines[vertical_index + 1][index - 1] + char + all_lines[vertical_index - 1][index + 1]

        possible_values = ["MAS", "SAM"]
        if diag1 in possible_values and diag2 in possible_values:
          xmas_appearances += 1

print(xmas_appearances)


