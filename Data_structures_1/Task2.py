import math

measures = [10, 10.1, 9.9, 9.6, 10.1, 9.9, 9.8, 9.9, 10.3, 10]

# average using only a loop, addition, and division
total = 0
for value in measures:
    total = total + value
average = total / len(measures)
print(f"Average: {average}")

# standard deviation using only a loop, addition, division, and math.sqrt
squared_diff_sum = 0
for value in measures:
    squared_diff_sum = squared_diff_sum + (value - average) * (value - average)
variance = squared_diff_sum / len(measures)
std_dev = math.sqrt(variance)
print(f"Standard Deviation: {std_dev:.2f}")