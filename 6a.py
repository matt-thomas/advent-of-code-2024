
map_lines = []
positions_visited = []

with open("6.txt", "r") as file:
    for line in file:
      map_lines.append(line.strip())

# Create the coordinate-based dictionary
grid = {
    (x, y): symbol
    for y, row in enumerate(map_lines)
    for x, symbol in enumerate(row)
}

# Find initial caret position.
for coordinates, value in grid.items():
  if value == "^":
    initial_pos = coordinates
    positions_visited.append(initial_pos)
    break

guard_pos = initial_pos
guard_orientation = 0
map_width = len(map_lines[0])
map_height = len(map_lines)

orientation_map = {
  0: (0, -1),
  90: (1, 0),
  180: (0, 1),
  270: (-1, 0),
}

def run_simulation(grid, positions_visited, guard_orientation, guard_pos):
  off_grid = False

  while not off_grid:
    move_tuple = orientation_map[guard_orientation]
    candidate_x, candidate_y = tuple(a + b for a, b in zip(guard_pos, move_tuple))

    # If we go off the grid, stop.
    if candidate_x < 0 or candidate_x >= map_width or candidate_y < 0 or candidate_y >= map_height:
      break

    # Get the character and determine if it's a valid location.
    next_char = grid[(candidate_x, candidate_y)]

    # If it's a valid move, update the guard's position and update the locations visited var.
    if next_char == "." or next_char == "^":
      positions_visited.append((candidate_x, candidate_y))
      guard_pos = (candidate_x, candidate_y)
    else:
      # Else move 90 degrees right, thank you modulus operator.
      guard_orientation = (guard_orientation + 90) % 360

  positions_visited = set(positions_visited)
  return positions_visited

positions_visited = run_simulation(grid, positions_visited, guard_orientation, guard_pos)
print(len(positions_visited))
