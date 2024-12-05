import re

all_lines = []
xmas_appearances = 0

with open("4-test.txt", "r") as file:
    for line in file:
        all_lines.append(line.strip())


# Define the directions to search for "XMAS"
directions = [
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right diagonal
    (1, -1),  # Down-Left diagonal
    (-1, 1),  # Up-Right diagonal
    (-1, -1), # Up-Left diagonal
]

def check_for_word(i, index, increment_line, increment_col):
    letters = ['X', 'M', 'A', 'S']
    for step in range(4):
        line_idx = i + increment_line * step
        col_idx = index + increment_col * step

        # Check boundaries
        if line_idx < 0 or line_idx >= len(all_lines):
            return 0
        line = all_lines[line_idx]
        if col_idx < 0 or col_idx >= len(line):
            return 0

        if line[col_idx] != letters[step]:
            return 0
    return 1

# Search for "XMAS" in all directions starting from each 'X'
for i in range(len(all_lines)):
    line = all_lines[i]
    for index in range(len(line)):
        if line[index] == 'X':
            for increment_line, increment_col in directions:
                xmas_appearances += check_for_word(i, index, increment_line, increment_col)

print(xmas_appearances)
