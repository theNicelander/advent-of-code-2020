from utils.files import read_groups_into_list

if __name__ == '__main__':
    data = read_groups_into_list("input.txt")
    print(data[:100])
