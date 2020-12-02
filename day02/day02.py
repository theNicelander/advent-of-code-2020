import pandas as pd


def apply_char_count_to_password(row):
    return row["password"].count(row["char"])


def apply_check_policy(row):
    if row["policy_min"] <= row["count"] <= row["policy_max"]:
        return True
    return False


def count_char_occurrences(df):
    df["char"] = df["char"].str.replace(":", "")
    df["count"] = df.apply(apply_char_count_to_password, axis=1)
    return df


def pipe_policy(df):
    cols = ["policy_min", "policy_max"]
    df[cols] = df["policy"].str.split("-", expand=True)
    df[cols] = df[cols].astype(int)
    df["valid"] = df.apply(apply_check_policy, axis=1)
    return df


def print_solution_1(df):
    valid_counts = df["valid"].value_counts()[True]
    print(f"Solution 1: {valid_counts}")
    return df


if __name__ == "__main__":
    data_file = "data.txt"
    df = pd.read_csv(data_file, sep=" ", names=["policy", "char", "password"])
    df = df.pipe(count_char_occurrences).pipe(pipe_policy).pipe(print_solution_1)
