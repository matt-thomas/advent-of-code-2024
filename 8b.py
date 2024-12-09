import itertools
from math import gcd

map_lines = []
antinode_positions = []

with open("8.txt", "r") as file:
    for line in file:
        map_lines.append(line.strip())

# Assemble an index of grid coordinates by symbol.
symbols_index = {}
map_width = len(map_lines[0])
print(map_width)
map_height = len(map_lines)
print(map_height)

for y, row in enumerate(map_lines):
    for x, symbol in enumerate(row):
        if symbol != "." and symbol != "#":
            try:
                symbols_index[symbol].append((x, y))
            except KeyError:
                symbols_index[symbol] = [(x, y)]

for symbol, positions in symbols_index.items():
    for (x1, y1), (x2, y2) in itertools.combinations(positions, 2):
        print(f"First item {x1}, {y1}")
        print(f"Second item {x2}, {y2}")

        dx = x2 - x1
        dy = y2 - y1
        g = gcd(dx, dy)
        dx_step = dx // g
        dy_step = dy // g

        # Use dx_step, dy_step in both directions starting from each antenna

        # From antenna (x1, y1) forward
        pos = (x1, y1)
        while True:
            pos = (pos[0] + dx_step, pos[1] + dy_step)
            if 0 <= pos[0] < map_width and 0 <= pos[1] < map_height:
                antinode_positions.append(pos)
            else:
                break

        # From antenna (x1, y1) backward
        pos = (x1, y1)
        while True:
            pos = (pos[0] - dx_step, pos[1] - dy_step)
            if 0 <= pos[0] < map_width and 0 <= pos[1] < map_height:
                antinode_positions.append(pos)
            else:
                break

        # From antenna (x2, y2) forward
        pos = (x2, y2)
        while True:
            pos = (pos[0] + dx_step, pos[1] + dy_step)
            if 0 <= pos[0] < map_width and 0 <= pos[1] < map_height:
                antinode_positions.append(pos)
            else:
                break

        # From antenna (x2, y2) backward
        pos = (x2, y2)
        while True:
            pos = (pos[0] - dx_step, pos[1] - dy_step)
            if 0 <= pos[0] < map_width and 0 <= pos[1] < map_height:
                antinode_positions.append(pos)
            else:
                break

# Convert to a set for uniqueness
antinode_positions = set(antinode_positions)
print(len(antinode_positions))
