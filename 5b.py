from collections import deque

ordering_rules = []
print_lines = []
running_total = 0
bad_total = 0

# Read input from file
with open("5.txt", "r") as file:
    for line in file:
        if "|" in line:
            ordering_rules.append(line.strip())
        elif "," in line:
            print_lines.append(line.strip())

def reorder_line_values(line_values):
    # Build the graph from ordering_rules
    graph = {value: [] for value in line_values}
    in_degree = {value: 0 for value in line_values}

    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num1 in line_values and num2 in line_values:
            graph[num1].append(num2)
            in_degree[num2] += 1

    # Perform topological sort using Kahn's algorithm
    queue = deque([value for value in line_values if in_degree[value] == 0])
    sorted_values = []
    while queue:
        value = queue.popleft()
        sorted_values.append(value)
        for neighbor in graph[value]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_values) != len(set(line_values)):
        # Cycle detected or unresolved dependencies
        print(f"Cannot reorder line due to cycle: {line_values}")
        return line_values  # Return original line if cannot resolve

    return sorted_values

# Process each print line
for print_line in print_lines:
    valid_line = True
    line_values = print_line.split(",")

    # Check if the line is valid
    for pos in range(len(line_values)):
        this_int = line_values[pos]
        preceding_ints = line_values[:pos]
        proceeding_ints = line_values[pos + 1:]

        # Validate ordering rules
        for rule in ordering_rules:
            num1, num2 = rule.split("|")
            if num1 == this_int and num2 in preceding_ints:
                valid_line = False
                break
            if num2 == this_int and num1 in proceeding_ints:
                valid_line = False
                break
        if not valid_line:
            break

    if valid_line:
        # Calculate middle number and update running total
        middle_index = len(line_values) // 2
        middle_member = line_values[middle_index]
        running_total += int(middle_member)
    else:
        # Reorder the line using topological sort
        print("REORDERING BAD LINE")
        print(f"Before: {line_values}")
        reordered_values = reorder_line_values(line_values)
        print(f"After: {reordered_values}")
        middle_index = len(reordered_values) // 2
        middle_member = reordered_values[middle_index]
        bad_total += int(middle_member)

# Print results
print("Running Total:", running_total)
print("Bad Total:", bad_total)
