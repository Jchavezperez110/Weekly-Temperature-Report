# CIS 105 - Weekend Project: Weekly Temperature Report
# Arrays, searching, and saving a report to a file
#
# Do not change the constant or the days array.

DAYS_IN_WEEK = 7
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

temps = []

# TODO 1: Ask for the high temperature for each day and store the
# answers in temps. Prompt format:
# "Enter the high temperature for Monday: "
for i in range(DAYS_IN_WEEK):
    temp = int(input(f"Enter the high temperature for {days[i]}: "))
    temps.append(temp)


# TODO 2: Compute the average high temperature for the week.
total_temp = 0
for i in range(DAYS_IN_WEEK):
    total_temp += temps[i]

average_high = total_temp / DAYS_IN_WEEK


# TODO 3: Find the position of the warmest day and the position of
# the coldest day (scan the array, keep the best position so far).
warmest_pos = 0
coldest_pos = 0

for i in range(1, DAYS_IN_WEEK):
    if temps[i] > temps[warmest_pos]:
        warmest_pos = i
    if temps[i] < temps[coldest_pos]:
        coldest_pos = i


# TODO 4: Count how many days had a high above the average.
above_avg_count = 0
for i in range(DAYS_IN_WEEK):
    if temps[i] > average_high:
        above_avg_count += 1


# TODO 5: Build the report as one string named report, in exactly
# this format:
#
# Weekly Temperature Report
# Monday: 68
# Tuesday: 72
# (one line per day)
# Average high: 70.9
# Warmest day: Wednesday (75)
# Coldest day: Friday (66)
# Days above average: 4
#
# Print the report.
report = "Weekly Temperature Report\n"
for i in range(DAYS_IN_WEEK):
    report += f"{days[i]}: {temps[i]}\n"

report += f"Average high: {average_high:.1f}\n"
report += f"Warmest day: {days[warmest_pos]} ({temps[warmest_pos]})\n"
report += f"Coldest day: {days[coldest_pos]} ({temps[coldest_pos]})\n"
report += f"Days above average: {above_avg_count}"

print()
print(report)
print()


# TODO 6: Ask the user for a temperature to search for.
# Find the FIRST day with exactly that high temperature.
# Print: First day with a high of 74 : Saturday
# or, if no day matches: No day had a high of 74
search_temp = int(input("Enter a temperature to search for: "))
found_pos = -1

for i in range(DAYS_IN_WEEK):
    if temps[i] == search_temp:
        found_pos = i
        break

if found_pos != -1:
    print(f"First day with a high of {search_temp} : {days[found_pos]}")
else:
    print(f"No day had a high of {search_temp}")


# TODO 7: Save the report string to a file named temps_report.txt
# Then print: Report saved to temps_report.txt
with open("temps_report.txt", "w") as out_file:
    out_file.write(report + "\n")

print("Report saved to temps_report.txt")