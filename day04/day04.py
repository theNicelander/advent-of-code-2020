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


def apply_part_1_validation(df):
    """Ignore cid column & remove all other entries with missing values"""
    df = df.drop("cid", axis=1).dropna()
    print("Solution 1: ", len(df))
    return df


def hgt_check(hgt):
    if hgt[-2:] == "cm":
        return 150 <= int(hgt[:-2]) <= 193
    if hgt[-2:] == "in":
        return 59 <= int(hgt[:-2]) <= 76
    return False


def apply_part_2_validation(df):
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    mask = (
        df["byr"].astype(int).between(1920, 2002)
        & df["iyr"].astype(int).between(2010, 2020)
        & df["eyr"].astype(int).between(2020, 2030)
        & df["hcl"].apply(lambda hcl: (len(hcl) == 7) & ("#" in hcl))
        & df["pid"].apply(lambda pid: len(pid) == 9)
        & df["ecl"].apply(lambda ecl: ecl in valid_ecls)
        & df["hgt"].apply(hgt_check)
    )
    df = df[mask]
    print("Solution 2: ", len(df))
    return df


if __name__ == "__main__":
    file = "input.txt"

    df = parse_input_to_df(file)

    df.pipe(apply_part_1_validation).pipe(apply_part_2_validation)
