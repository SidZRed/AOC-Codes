def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split('\n')
    return data


def calculate_difference(values):
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    return differences


def clean_and_convert(input_string):
    values = [int(i) for i in input_string.split() if i]
    return values[::-1]


def find_last_value(values):
    differences = calculate_difference(values)
    last_value = values[-1]

    while len(set(differences)) != 1:
        last_value += differences[-1]
        differences = calculate_difference(differences)

    last_value += differences[-1]
    return last_value


def main(file_path):
    data = read_file(file_path)
    total = sum(find_last_value(clean_and_convert(line)) for line in data)
    print(total)


if __name__ == "__main__":
    file_path = r"C:\Users\rolla\OneDrive\Desktop\Programming\Python_proj\input202309.txt"
    main(file_path)
