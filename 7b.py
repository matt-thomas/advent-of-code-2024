import itertools

all_lines = []
valid_line_values = []
operators_list = ['*', '+', '||']
possible_operators = len(operators_list)

with open("7.txt", "r") as file:
    for line in file:
      all_lines.append(line.strip())

for line in all_lines:
    line_total = int(line.split(':')[0].strip())
    line_values = [int(value) for value in line.split(':')[1].strip().split(' ')]

    # Calculate the total number of combinations
    possible_combinations = possible_operators ** (len(line_values) - 1)

    # Flag to indicate if a valid combination has been found
    found_valid_combo = False

    # Iterate over each possible combination of operators
    for ops in itertools.product(operators_list, repeat=(len(line_values)-1)):
        # Start with the first value
        result = line_values[0]

        # Apply each operator in sequence
        for op, val in zip(ops, line_values[1:]):
            if op == '+':
                result += val
            elif op == '*':
                result *= val
            elif op == '||':
                # TODO get previous value and concat with current value.
                result = int(str(result) + str(val))

        # Check if the result matches the line_total
        if result == line_total:
            valid_line_values.append(line_total)
            found_valid_combo = True
            break  # Break out of the ops loop

    if found_valid_combo:
        # Move on to the next line, skipping any remaining processing for this line
        continue

print(sum(valid_line_values))
