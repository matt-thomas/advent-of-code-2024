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

# Validate preceding rules
def validate_preceeding_rules(candidate_int, preceeding_ints):
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num1 == candidate_int and num2 in preceeding_ints:
            return False
    return True

# Validate proceeding rules
def validate_proceeding_rules(candidate_int, proceeding_ints):
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num2 == candidate_int and num1 in proceeding_ints:
            return False
    return True

# Process each print line
for print_line in print_lines:
    valid_line = True
    line_values = print_line.split(",")

    for pos in range(len(line_values)):
        this_int = line_values[pos]

        # Evaluate preceding integers against rules
        if pos > 0:
            preceeding_ints = line_values[0:pos]
            if not validate_preceeding_rules(this_int, preceeding_ints):
                valid_line = False
                break

        # Evaluate proceeding integers against rules
        if pos < len(line_values):
            proceeding_ints = line_values[(pos + 1):len(line_values)]
            if not validate_proceeding_rules(this_int, proceeding_ints):
                valid_line = False
                break

    # Calculate middle number and update totals
    middle_index = len(line_values) // 2
    middle_member = line_values[middle_index]

    if valid_line:
        running_total += int(middle_member)
    else:
        bad_total += int(middle_member)

# Print results
print(running_total)
print(bad_total)
