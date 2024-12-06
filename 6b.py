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
    visited_states = set()
    map_width = len(map_lines[0])
    map_height = len(map_lines)

    while True:
        state = (guard_pos, guard_orientation)
        if state in visited_states:
            # We have a loop!
            return None
        visited_states.add(state)

        move_tuple = orientation_map[guard_orientation]
        candidate_x, candidate_y = tuple(a + b for a, b in zip(guard_pos, move_tuple))

        # If we go off the grid, stop and return visited positions
        if candidate_x < 0 or candidate_x >= map_width or candidate_y < 0 or candidate_y >= map_height:
            break

        # Check the next character
        next_char = grid[(candidate_x, candidate_y)]

        # Valid move
        if next_char == "." or next_char == "^":
            positions_visited.append((candidate_x, candidate_y))
            guard_pos = (candidate_x, candidate_y)
        else:
            # Turn right
            guard_orientation = (guard_orientation + 90) % 360

    # Convert to a set to remove duplicates
    return set(positions_visited)

# Part One: Run the simulation as-is and print the number of visited positions.
part_one_visited = run_simulation(grid, positions_visited[:], guard_orientation, guard_pos)
if part_one_visited is not None:
    print("Part One:", len(part_one_visited))
else:
    # If it returned None, it means even the original setup caused a loop.
    # This is unexpected based on the puzzle description.
    print("Part One encountered a loop, which should not happen.")

# Part Two: Find all positions that would cause a loop if obstructed.
loop_causing_positions = []

# We'll test all positions that are currently walkable. We skip the guard's start position.
for (x, y), char in grid.items():
    if (x, y) == initial_pos:
        continue  # can't place obstruction at the guard's initial position
    if char == ".":
        # Temporarily change this cell to an obstacle
        original_char = grid[(x, y)]
        grid[(x, y)] = "#"

        # Re-run simulation
        test_visited = run_simulation(grid, [initial_pos], 0, initial_pos)

        if test_visited is None:
            # None means we detected a loop
            loop_causing_positions.append((x, y))

        # Restore original character
        grid[(x, y)] = original_char

print("Part Two:", len(loop_causing_positions))
