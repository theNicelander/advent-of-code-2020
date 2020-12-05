from utils.files import read_data_into_list

if __name__ == "__main__":
    file = "input.txt"
    data: list = read_data_into_list(file)
    print(data)
