ordering_rules = []
print_lines = []
running_total = 0
bad_total = 0

# Read input from file
with open("5-test.txt", "r") as file:
    for line in file:
        if "|" in line:
            ordering_rules.append(line.strip())
        elif "," in line:
            print_lines.append(line.strip())

# Validate preceding rules
def validate_preceding_rules(candidate_int, preceding_ints):
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num1 == candidate_int and num2 in preceding_ints:
            return False
    return True

# Validate preceding rules
def get_preceding_violators(candidate_int, preceding_ints):
    violations = []
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num1 == candidate_int and num2 in preceding_ints:
            violations.append(num2)
    return violations

# Validate proceeding rules
def get_proceeding_violators(candidate_int, proceeding_ints):
    violations = []
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num2 == candidate_int and num1 in proceeding_ints:
            print("rule violation")
            print(rule)
            violations.append(num1)
    return violations

# Validate proceeding rules
def validate_proceeding_rules(candidate_int, proceeding_ints):
    for rule in ordering_rules:
        num1, num2 = rule.split("|")
        if num2 == candidate_int and num1 in proceeding_ints:
            return False
    return True

# Reorder line values.
def reorder_line_values(line_values):
    reordered_values = line_values
    for pos in range(len(line_values)):
        this_int = line_values[pos]
        preceding_ints = line_values[0:pos]
        proceeding_ints = line_values[(pos + 1):len(line_values)]
        preceding_violations = get_preceding_violators(this_int, preceding_ints)
        proceeding_violations = get_proceeding_violators(this_int, proceeding_ints)
        if len(preceding_violations) + len(proceeding_violations) > 0:
            print(f"found a violator on {this_int}")
            if len(preceding_violations) > 0:
                print("preceding violation")
                print(preceding_violations)
                # Find last value in rearranged values and move the int to after it.
                reordered_values.pop(pos)
                last_violation_index = reordered_values.index(preceding_violations[-1])
                reordered_values.insert(last_violation_index + 1, this_int)
            elif len(proceeding_violations) > 0:
                print("proceding violation")
                print(proceeding_violations)
                # Find last value in rearranged values and move the int to after it.
                reordered_values.pop(pos)
                last_violation_index = reordered_values.index(proceeding_violations[0])
                reordered_values.insert(last_violation_index + 1, this_int)

    return reordered_values

# Process each print line
for print_line in print_lines:
    valid_line = True
    line_values = print_line.split(",")

    for pos in range(len(line_values)):
        this_int = line_values[pos]

        # Evaluate preceding integers against rules
        if pos > 0:
            preceding_ints = line_values[0:pos]
            if not validate_preceding_rules(this_int, preceding_ints):
                valid_line = False
                break

        # Evaluate proceeding integers against rules
        if pos < len(line_values):
            proceeding_ints = line_values[(pos + 1):len(line_values)]
            if not validate_proceeding_rules(this_int, proceeding_ints):
                valid_line = False
                break

    if valid_line:
        # Calculate middle number and update totals
        middle_index = len(line_values) // 2
        middle_member = line_values[middle_index]
        running_total += int(middle_member)
    else:
        # TODO Reorder the line correctly.
        print("REORDERING BAD LINE")
        print(line_values)
        line_values = reorder_line_values(line_values)
        print(line_values)
        middle_index = len(line_values) // 2
        middle_member = line_values[middle_index]
        bad_total += int(middle_member)

# Print results
print(running_total)
print(bad_total)
