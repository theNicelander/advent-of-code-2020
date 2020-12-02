import pandas as pd

df = pd.read_csv("data.txt").iloc[:,0].values

solutions = set()
for first_value in df:
    for second_value in df:

        sum = first_value + second_value
        if first_value + second_value == 2020:
            solutions.add(first_value * second_value)
print("first solution", solutions)

solutions = set()
for first_value in df:
    for second_value in df:
        for third_value in df:
            sum = first_value + second_value + third_value

            if sum == 2020:
                solutions.add(first_value * second_value * third_value)
print("second solution", solutions)
print("DONE")
