import itertools

map_lines = []
antinode_positions = []

with open("8.txt", "r") as file:
    for line in file:
      map_lines.append(line.strip())

# Assemble an index of grid coordinates by symbol.
symbols_index = {}
map_width = len(map_lines[0])
map_height = len(map_lines)

for y, row in enumerate(map_lines):
  for x, symbol in enumerate(row):
    if symbol != ".":
      try:
        symbols_index[symbol].append((x, y))
      except KeyError:
        symbols_index[symbol] = [(x, y)]

# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.
for symbol, positions in symbols_index.items():
  for (x1, y1), (x2, y2) in itertools.combinations(positions, 2):
      print(f"First item {x1}, {y1}")
      print(f"Second item {x2}, {y2}")

      diff1 = (x1 - x2, y1 - y2)
      diff2 = (x2 - x1, y2 - y1)

      pos1 = tuple(x + y for x, y in zip(diff1, (x1, y1)))
      if 0 < (pos1[0] + 1) <= map_width and 0 < (pos1[1] + 1) <= map_height:
        antinode_positions.append(pos1)

      pos2 = tuple(x + y for x, y in zip(diff2, (x2, y2)))
      if 0 < (pos2[0] + 1) <= map_width and 0 < (pos2[1] + 1) <= map_height:
        antinode_positions.append(pos2)

antinode_positions = set(antinode_positions)
print(len(antinode_positions))
