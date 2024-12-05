all_reports = []
safe_reports = 0

with open("2.txt", "r") as file:
    for line in file:
        line_levels = [int(value) for value in line.strip().split(' ')]
        all_reports.append(line_levels)

print(len(all_reports))

# A report only counts as safe if both of the following are true:

for line_levels in all_reports:
    print(line_levels)
    faults = 0

    if line_levels[0] - line_levels[1] > 0:
        # decreasing
        increment = -1
    else:
        # increasing
        increment = 1

    # The levels are either all increasing or all decreasing.
    for i in range(len(line_levels)):
      if i + 1 < len(line_levels):
        this_value = line_levels[i]
        next_value = line_levels[i + 1]
        diff = abs(this_value - next_value)

        # Any two adjacent levels differ by at least one and at most three.
        if diff < 1 or diff > 3:
           faults += 1

        # The levels are either all increasing or all decreasing.
        if (this_value - next_value > 0 and increment == 1) or (this_value - next_value < 0 and increment == -1):
           faults += 1

    if faults < 2:
       safe_reports += 1

print(safe_reports)

