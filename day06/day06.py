from utils.files import read_groups_into_list
from collections import Counter

def read_file(path):
    with open(path) as f:
        return f.read().split("\n\n")


def sum_unique_answers(data: list) -> int:
    data = [g.replace("\n", "") for g in data]
    unique_answers = [len(set(group)) for group in data]
    return sum(unique_answers)




if __name__ == "__main__":
    data = read_file("input.txt", clean_newline=False)

    print("Part 1", sum_unique_answers(data))
