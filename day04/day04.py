import pandas as pd


def parse_input_to_df(path) -> pd.DataFrame:
    raw_input = read_raw_input(path)
    passport_strings: list = convert_to_single_string_per_passport(raw_input)
    dictionaries = convert_passports_to_dictionaries(passport_strings)
    return pd.DataFrame(dictionaries)


def read_raw_input(path: str) -> list:
    with open(path) as f:
        return f.read().splitlines()


def convert_to_single_string_per_passport(lines):
    list_of_strings = [""]
    for line in lines:
        if line == "":
            list_of_strings.append("")
        list_of_strings[-1] = list_of_strings[-1] + " " + line
    return list_of_strings


def convert_passports_to_dictionaries(data):
    passports = [passport.split(" ") for passport in data]
    passport_dicts = []
    for passport in passports:
        passport_dict = {str(entry[:3]): str(entry[4:]) for entry in passport if entry}
        passport_dicts.append(passport_dict)
    return passport_dicts


def apply_is_valid_passport(row):
    if row["no_missing"] == 0:
        return True
    return False


if __name__ == "__main__":
    file = "input.txt"

    df = parse_input_to_df(file)
    df = df.drop("cid", axis=1)

    df_valid = df.dropna()
    print(len(df_valid))
