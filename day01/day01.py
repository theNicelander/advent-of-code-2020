from itertools import combinations
import pandas as pd
import numpy as np


def print_prod_of_entries_that_sum_to_num(data: list, iterations: int, num: int = 2020):

    all_combinations = combinations(data, iterations)
    for combination in all_combinations:
        if sum(combination) == num:
            product = np.prod(combination)
            print(iterations, product)
            break


if __name__ == "__main__":
    data = pd.read_csv("data.txt").iloc[:, 0].values
    print_prod_of_entries_that_sum_to_num(data, 2, 2020)
    print_prod_of_entries_that_sum_to_num(data, 3, 2020)
