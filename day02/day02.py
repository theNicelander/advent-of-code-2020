import pandas as pd


def apply_char_count_to_password(row):
    return row["password"].count(row["char"])


def apply_check_policy_1(row):
    if row["policy_min"] <= row["count"] <= row["policy_max"]:
        return True
    return False


def count_char_occurrences(df):
    df["char"] = df["char"].str.replace(":", "")
    df["count"] = df.apply(apply_char_count_to_password, axis=1)
    return df


def policy_1(df):
    cols = ["policy_min", "policy_max"]
    df[cols] = df["policy"].str.split("-", expand=True)
    df[cols] = df[cols].astype(int)
    df["valid_1"] = df.apply(apply_check_policy_1, axis=1)
    return df


def print_solution(df, solution:int):
    valid_counts = df[f"valid_{solution}"].value_counts()[True]
    print(f"Solution {solution}: {valid_counts}")
    return df


def apply_check_policy_2(row):
    first_index = row["policy_min"] - 1
    second_index = row["policy_max"] - 1

    first_valid = row["password"][first_index] == row["char"]
    second_valid = row["password"][second_index] == row["char"]

    if first_valid ^ second_valid:
        return True
    return False


def policy_2(df):
    df["valid_2"] = df.apply(apply_check_policy_2, axis=1)
    return df


def print_df_head(df):
    print("--------------------------------")
    print(df.head().loc[:, :"policy_max"])
    print(df.head().loc[:, "valid_1":])


if __name__ == "__main__":
    data_file = "data.txt"
    df = pd.read_csv(data_file, sep=" ", names=["policy", "char", "password"])
    df = (
        df.pipe(count_char_occurrences)
        .pipe(policy_1)
        .pipe(print_solution, solution=1)
        .pipe(policy_2)
        .pipe(print_solution, solution=2)
    )

    print_df_head(df)
