import pandas as pd

data = pd.read_csv("data.txt").iloc[:, 0].values

solutions = set()
for first_value in data:
    for second_value in data:

        sum = first_value + second_value
        if first_value + second_value == 2020:
            solutions.add(first_value * second_value)
print("first solution", solutions)

solutions = set()
for first_value in data:
    for second_value in data:
        for third_value in data:
            sum = first_value + second_value + third_value

            if sum == 2020:
                solutions.add(first_value * second_value * third_value)
print("second solution", solutions)
print("DONE")
